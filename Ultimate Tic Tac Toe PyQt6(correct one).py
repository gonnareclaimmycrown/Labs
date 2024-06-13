import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QLabel, QFileDialog, QLineEdit, QMenu, QMenuBar, QMainWindow, QVBoxLayout, QColorDialog, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon, QAction, QImage
from PyQt6.QtCore import QSize, Qt, QBuffer, QByteArray
import base64 

class UltimateTicTacToe(QWidget):
    def __init__(self, menu):
        super().__init__()
        self.initUI()
        self.setEnabled(False)
        self.player_turn = 'X'
        self.next_board = None
        self.menu = menu

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.boards = [[TicTacToe(self, i, j) for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                grid.addWidget(self.boards[i][j], i, j)

    def make_move(self, board, button):
        def inner():
            if button.text() == '':
                button.setText(self.player_turn)
                button.setStyleSheet(f"color: {menu.getPlayerColor()}; font-size: 15px;") 
                if self.player_turn == 'X':
                    self.player_turn = 'O'
                else:
                    self.player_turn = 'X'
                self.next_board = (button.row, button.col)
                self.update_boards()
                winner = board.check_winner()
                if winner is not None:
                    if (button.row, button.col) == (board.row, board.col):
                        self.enable_boards_without_winner()
                    self.replace_board(board, winner)
                    ultimate_winner = self.check_ultimate_winner()
                    if ultimate_winner is not None:
                        self.declare_winner(ultimate_winner)
                if board.check_tie():
                    self.declare_the_end()
                #board.check_overall_tie()
        return inner
    

    def enable_boards_without_winner(self):
        for i in range(3):
            for j in range(3):
                if not isinstance(self.boards[i][j], QPushButton) and self.boards[i][j].winner is None:
                    self.boards[i][j].setEnabled(True)


    def declare_the_end(self):
        msg = QMessageBox()
        msg.setText(f"I guess this is the end")
        msg.exec()
        menu.reset_game()

    def update_boards(self):
        for i in range(3):
            for j in range(3):
                if isinstance(self.boards[i][j], QPushButton):
                    self.boards[i][j].setEnabled(False)
                elif self.next_board is None or self.next_board == (i, j):
                    self.boards[i][j].setEnabled(True)
                elif self.next_board is not None and isinstance(self.boards[self.next_board[0]][self.next_board[1]], TicTacToe) and self.boards[self.next_board[0]][self.next_board[1]].winner is not None:
                    if self.boards[i][j].winner is None:
                        self.boards[i][j].setEnabled(True)
                    else:
                        self.boards[i][j].setEnabled(False)
                elif isinstance(self.boards[self.next_board[0]][self.next_board[1]], QPushButton):
                    self.boards[i][j].setEnabled(True)
                else:
                    self.boards[i][j].setEnabled(False)

    def replace_board(self, board, winner):
        i, j = board.row, board.col
        self.boards[i][j].deleteLater()
        self.boards[i][j] = QPushButton(winner)
        self.boards[i][j].setStyleSheet(f"color: {menu.getPlayerColor1()}; font-size: 100px;")
        self.boards[i][j].setEnabled(False)
        self.layout().addWidget(self.boards[i][j], i, j)

    def check_ultimate_winner(self):
        for i in range(3):
            if self.check_line_winner([(i, 0), (i, 1), (i, 2)]):
                return self.get_winner_from_board(i, 0)

        for j in range(3):
            if self.check_line_winner([(0, j), (1, j), (2, j)]):
                return self.get_winner_from_board(0, j)

        if self.check_line_winner([(0, 0), (1, 1), (2, 2)]):
            return self.get_winner_from_board(1, 1)
        if self.check_line_winner([(0, 2), (1, 1), (2, 0)]):
            return self.get_winner_from_board(1, 1)

        return None

    def check_line_winner(self, positions):
        first_board = self.boards[positions[0][0]][positions[0][1]]
        if isinstance(first_board, QPushButton):
            first_winner = first_board.text()
        elif isinstance(first_board, TicTacToe) and first_board.winner is not None:
            first_winner = first_board.winner
        else:
            return False

        for pos in positions[1:]:
            board = self.boards[pos[0]][pos[1]]
            if isinstance(board, QPushButton):
                if board.text() != first_winner:
                    return False
            elif isinstance(board, TicTacToe) and board.winner is not None:
                if board.winner != first_winner:
                    return False
            else:
                return False
        return True

    def get_winner_from_board(self, i, j):
        board = self.boards[i][j]
        if isinstance(board, QPushButton):
            return board.text()
        elif isinstance(board, TicTacToe):
            return board.winner
        return None
    
    def declare_winner(self, winner):
        msg = QMessageBox()
        msg.setText(f"Player {menu.alias if winner == 'X' else menu.alias1} wins!")
        msg.exec()
        menu.reset_game()

    def clear_fields(self):
        for i in range(3):
            for j in range(3):
                if isinstance(self.boards[i][j], QPushButton):
                    self.boards[i][j].deleteLater()
                    self.boards[i][j] = TicTacToe(self, i, j)
                    self.layout().addWidget(self.boards[i][j], i, j)
                else:
                    self.boards[i][j].clear_board()

    def save_game(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json);;All Files (*)")
        if file_path:
            game_state = {
                'player_info': menu.get_player_info(),
                'player_turn': self.player_turn,
                'next_board': self.next_board,
                'boards': [
                    [
                        board.get_state() if isinstance(board, TicTacToe) else {'button': True,'winner': board.text()}
                        for board in row
                    ]
                    for row in self.boards
                ]
            }
            with open(file_path, 'w') as file:
                json.dump(game_state, file, indent=2)

    def load_game(self):
        menu.reset_game()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load File", "", "JSON Files (*.json);;All Files (*)")
        if file_path:
            with open(file_path, 'r') as file:
                game_state = json.load(file)
                menu.set_player_info(game_state['player_info'])
            self.player_turn = game_state['player_turn']
            self.next_board = tuple(game_state['next_board']) if game_state['next_board'] is not None else None
            for i, row in enumerate(game_state['boards']):
                for j, board_state in enumerate(row):
                    if 'button' in board_state:
                        self.replace_board(self.boards[i][j], board_state['winner'])
                    else:
                        self.boards[i][j].deleteLater()
                        self.boards[i][j] = TicTacToe(self, i, j)
                        self.boards[i][j].set_state(board_state)
                        self.layout().addWidget(self.boards[i][j], i, j)
            self.update_boards()



class TicTacToe(QWidget):
    def __init__(self, parent, row, col):
        super().__init__()
        self.parent = parent
        self.row = row
        self.col = col
        self.initUI()
        self.player_turn = 'X'
        self.winner = None 

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.buttons = [[QPushButton('') for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                button.row = i
                button.col = j
                grid.addWidget(button, i, j)
                button.clicked.connect(self.parent.make_move(self, button))

    def check_tie(self):
        for row in self.buttons:
            for button in row:
                if button.text() == '':
                    return False
        return True
    
    def clear_board(self):
        for row in self.buttons:
            for button in row:
                button.setText("")
                button.setEnabled(True)
            

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != '':
                self.winner = self.buttons[i][0].text()
                print(self.winner)
                return self.winner

        for i in range(3):
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != '':
                self.winner = self.buttons[0][i].text()
                print(self.winner)
                return self.winner

        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != '':
            self.winner = self.buttons[0][0].text()
            print(self.winner)
            return self.winner
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != '':
            print(self.winner)
            self.winner = self.buttons[0][2].text()
            return self.winner

        return None
    
    def get_state(self):
        return {
            'buttons': [
                [button.text() for button in row]
                for row in self.buttons
            ],
            'player_turn': self.player_turn,
            'winner': self.winner if hasattr(self, 'winner') else None
        }

    def set_state(self, state):
        self.player_turn = state['player_turn']
        self.winner = state['winner']
        for i, row in enumerate(state['buttons']):
            for j, text in enumerate(row):
                button = self.buttons[i][j]
                button.setText(text)
                button.setEnabled(text == '')


    #def check_overall_tie(self):
     #   for i in range(3):
      #      for j in range(3):
       #         if all(self.buttons[i][j].parent.check_winner) and not self.check_overall_winner:
        #            self.parent.declare_the_end()


class Menu(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.field = UltimateTicTacToe(self)
            layout = QGridLayout()

            self.alias = ""
            self.alias1 = ""
            self.colors = {"X": "black", "O": "black"}
            self.nicknameLineEdit = QLineEdit()
            layout.addWidget(self.nicknameLineEdit, 2, 0)

            self.confirmButton = QPushButton("Confirm Nickname")
            self.confirmButton.clicked.connect(self.confirm_nickname)
            layout.addWidget(self.confirmButton, 3, 0)

            self.uploadButton = QPushButton("Upload Photo")
            self.uploadButton.clicked.connect(self.upload_photo)
            layout.addWidget(self.uploadButton, 1, 0)

            self.photoLabel = QLabel()
            layout.addWidget(self.photoLabel, 0, 0)

            layout.addWidget(self.field, 0, 1)

            self.nicknameLineEdit1 = QLineEdit()
            layout.addWidget(self.nicknameLineEdit1, 2, 2)

            self.confirmButton1 = QPushButton("Confirm Nickname")
            self.confirmButton1.clicked.connect(self.confirm_nickname1)
            layout.addWidget(self.confirmButton1, 3, 2)

            self.uploadButton1 = QPushButton("Upload Photo")
            self.uploadButton1.clicked.connect(self.upload_photo1)
            layout.addWidget(self.uploadButton1, 1, 2)

            self.photoLabel1 = QLabel()
            layout.addWidget(self.photoLabel1, 0, 2)

            self.startButton = QPushButton("Let's go!")
            self.startButton.clicked.connect(self.start_game)
            layout.addWidget(self.startButton, 1, 1)

            self.resetButton = QPushButton("Reset")
            self.resetButton.clicked.connect(self.reset_game)
            layout.addWidget(self.resetButton, 2, 1)

            self.setLayout(layout)

            layout2 = QVBoxLayout(self)
            menuBar = QMenuBar(self)
            fileMenu = menuBar.addMenu('File')
            editMenu = menuBar.addMenu('Edit')

            saveButton = QAction(QIcon('save.png'), 'Save', self)
            loadButton = QAction(QIcon('load.png'), 'Load', self)
            fileMenu.addAction(saveButton)
            fileMenu.addAction(loadButton)

            changeXColor = QAction(QIcon('color.png'), 'Change X Color', self)
            changeOColor = QAction(QIcon('color.png'), 'Change O Color', self)
            editMenu.addAction(changeXColor)
            editMenu.addAction(changeOColor)
            changeXColor.triggered.connect(self.changeXColor)
            changeOColor.triggered.connect(self.changeOColor)
            saveButton.triggered.connect(self.field.save_game)
            loadButton.triggered.connect(self.field.load_game)

            self.setGeometry(300, 300, 300, 200)
            layout.setMenuBar(menuBar)
            self.setLayout(layout2)


        def confirm_nickname(self):
            self.nickname = self.nicknameLineEdit.text()
            print(f"Nickname confirmed: {self.nickname}")
            self.alias = self.nickname

        def upload_photo(self):
            filename, _ = QFileDialog.getOpenFileName()
            if filename:
                pixmap = QPixmap(filename)
                self.photoLabel.setPixmap(pixmap.scaled(250, 250))
                
        def confirm_nickname1(self):
            self.nickname1 = self.nicknameLineEdit1.text()
            print(f"Nickname confirmed: {self.nickname1}")
            self.alias1 = self.nickname1
 
        def upload_photo1(self):
            filename, _ = QFileDialog.getOpenFileName()
            if filename:
                pixmap = QPixmap(filename)
                self.photoLabel1.setPixmap(pixmap.scaled(250, 250))

        def start_game(self):
            self.confirmButton.setEnabled(False)
            self.confirmButton1.setEnabled(False)
            self.nicknameLineEdit.setEnabled(False)
            self.nicknameLineEdit1.setEnabled(False)
            self.uploadButton.setEnabled(False)
            self.uploadButton1.setEnabled(False)
            self.startButton.setEnabled(False)
            self.field.setEnabled(True)
            self.field.player_turn = 'X'
            for i in range(3):
                for j in range(3):
                    self.field.boards[i][j].setEnabled(True)
            if self.alias == "":
                self.alias = "X"
            if self.alias1 == "":
                self.alias1 = "O"

        def reset_game(self):
            self.confirmButton.setEnabled(True)
            self.confirmButton1.setEnabled(True)
            self.nicknameLineEdit.setEnabled(True)
            self.nicknameLineEdit1.setEnabled(True)
            self.uploadButton.setEnabled(True)
            self.uploadButton1.setEnabled(True)
            self.startButton.setEnabled(True)
            self.field.setEnabled(False)
            self.nicknameLineEdit.clear
            self.nicknameLineEdit1.clear
            self.photoLabel.clear
            self.photoLabel1.clear
            self.field.clear_fields()
            self.field.player_turn = 'X'
            self.field.next_board = None
            self.field.update_boards()
            self.colors = {"X": "black", "O": "black"}



        def changeXColor(self):
            color = QColorDialog.getColor()
            if color.isValid():
                self.colors['X'] = color.name()


        def changeOColor(self):
            color = QColorDialog.getColor()
            if color.isValid():
                self.colors['O'] = color.name()

        def getPlayerColor(self):
            if self.field.player_turn == 'X':
                return self.colors['X']
            else:
                return self.colors['O']
            
        def getPlayerColor1(self):
            if self.field.player_turn == 'O':
                return self.colors['X']
            else:
                return self.colors['O']
            
        def get_player_info(self):
            player_info = {
                'player1': {
                    'nickname': self.nicknameLineEdit.text(),
                    'photo': None
                },
                'player2': {
                    'nickname': self.nicknameLineEdit1.text(),
                    'photo': None
                }
            }
            for player_key, widgets in [('player1', (self.photoLabel, self.nicknameLineEdit)),
                                ('player2', (self.photoLabel1, self.nicknameLineEdit1))]:
                photo_label, _ = widgets
                if photo_label.pixmap():
                    buffer = QBuffer()
                    buffer.open(QBuffer.OpenModeFlag.ReadWrite)
                    photo_label.pixmap().save(buffer, "PNG")
                    player_info[player_key]['photo'] = bytes(buffer.data().toBase64()).decode('utf-8')
            return player_info

        def set_player_info(self, player_info):
            self.nicknameLineEdit.setText(player_info['player1']['nickname'])
            self.nicknameLineEdit1.setText(player_info['player2']['nickname'])
            if player_info['player1']['photo']:
                image = QImage()
                image.loadFromData(base64.b64decode(player_info['player1']['photo']))
                self.photoLabel.setPixmap(QPixmap(image))
            if player_info['player2']['photo']:
                image = QImage()
                image.loadFromData(base64.b64decode(player_info['player2']['photo']))
                self.photoLabel1.setPixmap(QPixmap(image))

if __name__ == '__main__':
    app = QApplication([])
    menu = Menu()
    menu.show()
    sys.exit(app.exec())
