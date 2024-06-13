import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QLabel, QFileDialog, QLineEdit, QMenu, QMenuBar, QMainWindow, QVBoxLayout, QColorDialog, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import QSize, Qt

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
                    ultimate_winner = self.check_win()
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
        self.boards[i][j].setStyleSheet(f"color: {menu.getPlayerColor()}; font-size: 100px;")
        self.boards[i][j].setEnabled(False)
        self.layout().addWidget(self.boards[i][j], i, j)

    def check_win(self):
        print("Checking for a winner...")
        for i in range(3):
            for j in range(3):
                if (isinstance(self.boards[i][j], TicTacToe) or isinstance(self.boards[i][j], str)):
                    winner = self.boards[i][j].check_winner()
                    if winner:
                        print("xddd")
                        return winner

        
        for row in range(3):
            if (isinstance(self.boards[row][0], TicTacToe) or isinstance(self.boards[row][0], str)) and \
            (isinstance(self.boards[row][1], TicTacToe) or isinstance(self.boards[row][1], str)) and \
            (isinstance(self.boards[row][2], TicTacToe) or isinstance(self.boards[row][2], str)):
                if self.boards[row][0].winner is not None and \
                self.boards[row][0].winner == self.boards[row][1].winner == self.boards[row][2].winner:
                    print("row winner:", winner)
                    return self.boards[row][0].winner


        for col in range(3):
            if (isinstance(self.boards[col][0], TicTacToe) or isinstance(self.boards[col][0], str)) and \
            (isinstance(self.boards[col][1], TicTacToe) or isinstance(self.boards[col][1], str)) and \
            (isinstance(self.boards[col][2], TicTacToe) or isinstance(self.boards[col][2], str)):
                if self.boards[col][0].winner == self.boards[col][1].winner == self.boards[col][2].winner != None:
                    print("col winner:", winner)
                    return self.boards[row][0].winner

        if isinstance(self.boards[0][0], TicTacToe) and isinstance(self.boards[1][1], TicTacToe) and isinstance(self.boards[2][2], TicTacToe):
            if self.boards[0][0].check_winner() == self.boards[1][1].check_winner() == self.boards[2][2].check_winner() != None:
                print("diagonal winner:", winner)
                return self.boards[0][0].check_winner()
        if isinstance(self.boards[0][2], TicTacToe) and isinstance(self.boards[1][1], TicTacToe) and isinstance(self.boards[2][0], TicTacToe):
            if self.boards[0][2].check_winner() == self.boards[1][1].check_winner() == self.boards[2][0].check_winner() != None:
                print("Diagonal winner:", winner)
                return self.boards[0][2].check_winner()
        print("lox")
        return None
    
    def check_winner(self):
        for board_row in self.boards:
            for board in board_row:
                winner = board.check_winner()
                if winner is not None:
                    return winner
        return None
    
    def check_winner1(self):
        for i in range(3):
            for j in range(3):
                winner = self.boards[i][j].check_winner()
                if winner:
                    return winner

        for row in range(3):
            if self.boards[row][0].winner == self.boards[row][1].winner == self.boards[row][2].winner != None:
                return self.boards[row][0].winner

        for col in range(3):
            if self.boards[0][col].winner == self.boards[1][col].winner == self.boards[2][col].winner != None:
                return self.boards[0][col].winner

        if self.boards[0][0].winner == self.boards[1][1].winner == self.boards[2][2].winner != None:
            return self.boards[0][0].winner
        if self.boards[0][2].winner == self.boards[1][1].winner == self.boards[2][0].winner != None:
            return self.boards[0][2].winner
            return None 
    
    def declare_winner(self, winner):
        msg = QMessageBox()
        msg.setText(f"Player {menu.alias if winner == 'X' else menu.alias1} wins!")
        msg.exec()
        menu.reset_game()

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.boards[i][j].deleteLater()
                self.boards[i][j] = TicTacToe(self, i, j)
                self.layout().addWidget(self.boards[i][j], i, j)
        self.player_turn = 'X'



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
    
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")
                self.buttons[i][j].setEnabled(True)
        self.player_turn = 'X'

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


    #def check_overall_tie(self):
     #   for i in range(3):
      #      for j in range(3):
       #         if all(self.buttons[i][j].parent.check_winner) and not self.check_overall_winner:
        #            self.parent.declare_the_end()


class Menu(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
            self.Ultimate_Tic_Tac_Toe = UltimateTicTacToe(self)

        def initUI(self):
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

            self.field = UltimateTicTacToe(Menu)
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
            Ultimate_Tic_Tac_Toe.player_turn = 'X'
            for i in range(3):
                for j in range(3):
                    self.field.boards[i][j].setEnabled(True)
            if self.alias1 == "":
                self.alias1 = "X"
            if self.alias == "":
                self.alias = "O"

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
            for i in range(3):
                for j in range(3):
                    if isinstance(self.field.boards[i][j], TicTacToe):
                        self.field.boards[i][j].reset()
            Ultimate_Tic_Tac_Toe.player_turn = 'X'
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
            if Ultimate_Tic_Tac_Toe.player_turn == 'X':
                print(self.colors['X'])
                print(self.colors['O'])
                return self.colors['X']
            else:
                print(self.colors['X'])
                print(self.colors['O'])
                return self.colors['O']


if __name__ == '__main__':
    app = QApplication([])
    menu = Menu()
    Ultimate_Tic_Tac_Toe = UltimateTicTacToe(menu)
    menu.show()
    sys.exit(app.exec())
