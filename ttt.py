import json
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QMessageBox,QColorDialog,QFileDialog,QLabel,QHBoxLayout,QLineEdit
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction,QPixmap
from PyQt6.QtWidgets import QMenuBar, QMenu, QWidget

class SmallField(QWidget):
    def __init__(self, parent, row, column):
        super().__init__(parent)
        self.fieldLayout = QGridLayout()
        self.buttons = [[QPushButton() for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.row = row
        self.column = column
        self.parent = parent
        self.winButton = QPushButton()
        self.winButton.setVisible(False)
        self.winButton.setFixedSize(QSize(246, 228))
        self.fieldLayout.addWidget(self.winButton)
        for i in range(3):
            for j in range(3): 
                button = self.buttons[i][j]
                button.setFixedSize(QSize(82, 75))
                button.setStyleSheet("font-size: 35px;") 
                button.clicked.connect(lambda _, row = i, column = j: self.handleClick(row, column))
                self.fieldLayout.addWidget(button, i, j)
        self.setLayout(self.fieldLayout)
        self.setEnabled(False)
        
    def SetWinner(self):
        for i in range(3):
            for j in range(3):
                if self.winner:
                    self.buttons[i][j].setVisible(False)
        self.winButton.setVisible(True)
        self.winButton.setText(self.winner)
        self.winButton.setEnabled(False)
        self.winButton.setStyleSheet(f"color: {self.parent.getColor(self.winner)}; font-size: 100px;")


   
    def handleClick(self, row, column):
        if self.buttons[row][column].text() == "" and self.winner is None:
            if self.parent.activeField is None or self.parent.activeField == (self.row, self.column):
                self.buttons[row][column].setText(self.parent.currentPlayer)
                self.buttons[row][column].setStyleSheet(f"color: {self.parent.getCurrentPlayerColor()}; font-size: 35px;") 
                if self.checkWinner(row, column):
                    self.winner = self.parent.currentPlayer
                    self.SetWinner()
                    self.disableField()
                    self.parent.checkOverallWinner()
                    self.parent.checkOverallTie()
                elif self.checkTie(row, column):
                    msg = QMessageBox()
                    msg.setText(f"Noone wins!")
                    msg.exec()
                    self.parent.resetGame()

                self.parent.switchPlayer()
                self.parent.MakeNextFieldActive(row, column)

    def checkWinner(self, row, column):
        player = self.parent.currentPlayer
        if all(self.buttons[row][i].text() == player for i in range(3)):
            return True
        if all(self.buttons[i][column].text() == player for i in range(3)):
            return True
        if row == column and all(self.buttons[i][i].text() == player for i in range(3)):
            return True
        if row + column == 2 and all(self.buttons[i][2-i].text() == player for i in range(3)):
            return True
        return False
    
    def checkTie(self, row, column):
        if not self.checkWinner(row, column) and not self.CheckIfEmpty():
            return True
        return False

    def CheckIfEmpty(self):
        for i in range(3):
            if not all(self.buttons[i][j].text() for j in range(3)):
                return True
        return False

    def disableField(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setEnabled(False)

    def enableField(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j].text() == "":
                    self.buttons[i][j].setEnabled(True)
                






class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The root af all my pain")
        self.currentPlayer = "X"
        self.colors = {"X": "black", "O": "black"}
        self.centralWidget = QWidget()
        self.mainLayout = QGridLayout(self.centralWidget)
        self.alias1 = ""
        self.inputAlias1 = QLineEdit()

        self.enterButton1 = QPushButton("Confirm your nickname")
        self.enterButton1.clicked.connect(self.setAlias)

        self.loadButton1 = QPushButton("Upload your photo")
        self.loadButton1.clicked.connect(self.loadImage)
        self.resetbutton = QPushButton("Reset")
        self.resetbutton.clicked.connect(self.resetGame)
        self.surButton = QPushButton("Surrender")
        self.surButton.clicked.connect(self.Surrender)


        self.image1 = QLabel()
        self.image1.setFixedSize(350, 350)

    

        self.rightLayout = QVBoxLayout()
        self.alias2 = ""
        self.inputAlias2 = QLineEdit()

        self.inputAlias1.setFixedWidth(350)
        self.inputAlias2.setFixedWidth(350)

        self.enterButton2 = QPushButton("Confirm your nickname")
        self.enterButton2.clicked.connect(self.setAlias1)

        self.loadButton2 = QPushButton("Upload your photo")
        self.loadButton2.clicked.connect(self.loadImage1)

        self.image2 = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.image2.setFixedSize(350, 350)

        self.startButton = QPushButton("Let's play!")
        self.startButton.clicked.connect(self.startGame)

        self.gameLayout = QGridLayout(self.centralWidget)

        self.SmallFields = [[SmallField(self, i, j) for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.gameLayout.addWidget(self.SmallFields[i][j], i+1, j+1)

        self.sideLayout1 = QVBoxLayout(self.centralWidget)
        self.sideLayout2 = QVBoxLayout(self.centralWidget)

        self.sideLayout1.addWidget(self.image1)
        self.sideLayout1.addWidget(self.loadButton1)
        self.sideLayout1.addWidget(self.inputAlias1)
        self.sideLayout1.addWidget(self.enterButton1)
        self.sideLayout1.addWidget(self.resetbutton)

        self.sideLayout2.addWidget(self.image2)
        self.sideLayout2.addWidget(self.loadButton2)
        self.sideLayout2.addWidget(self.inputAlias2)
        self.sideLayout2.addWidget(self.enterButton2)
        self.sideLayout2.addWidget(self.surButton)

        
        self.mainLayout.addLayout(self.gameLayout, 0, 1)
        self.mainLayout.addLayout(self.sideLayout1, 0, 0)
        self.mainLayout.addLayout(self.sideLayout2, 0, 2)
        #self.mainLayout.addWidget(self.resetbutton, 1, 0)
        self.mainLayout.addWidget(self.startButton, 1, 1)
        #self.mainLayout.addWidget(self.surButton, 1, 2)
        



        self.activeField = None
        
        self.MakeAllFieldsActive()
        self.setCentralWidget(self.centralWidget)

        menu = self.menuBar()

        button1 = QAction("&Save", self)
        button1.triggered.connect(self.saveGame)

        button2 = QAction("&Load", self)
        button2.triggered.connect(self.loadGame)

        button3=QAction("&change X Color",self)
        button3.triggered.connect(self.changeXColor)
        button4=QAction("&change O Color",self)
        button4.triggered.connect(self.changeOColor)

        fileMenu1 = menu.addMenu("&File")
        fileMenu1.addAction(button1)
        fileMenu1.addAction(button2)

        fileMenu2 = menu.addMenu("&Style")
        fileMenu2.addAction(button3)
        fileMenu2.addAction(button4)

    def loadImage1(self):
        file = QFileDialog(wnd)
        fileName = file.getOpenFileName()[0]
        pixmap = QPixmap(fileName)
        self.image2.setPixmap(pixmap.scaled(self.image2.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def setAlias1(self):
        self.alias2 = self.inputAlias2.text()

    def loadImage(self):
        file = QFileDialog(wnd)
        fileName = file.getOpenFileName()[0]
        pixmap = QPixmap(fileName)
        self.image1.setPixmap(pixmap.scaled(self.image1.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def setAlias(self):
        self.alias1 = self.inputAlias1.text()

    def getCurrentPlayerColor(self):
        return self.colors[self.currentPlayer]

    def getColor(self, player):
        return self.colors[player]

    def MakeAllFieldsEnabled(self, enabled):
        for row in self.SmallFields:
            for grid in row:
                grid.setEnabled(enabled)


    def MakeAllFieldsActive(self):
        for row in self.SmallFields:
            for grid in row:
                grid.enableField()


    def startGame(self):
        self.activeField = None
        self.UpdateActiveFields()
        self.MakeAllFieldsEnabled(True)
        if self.alias1 == "":
            self.alias1 = "X"
        if self.alias2 == "":
            self.alias2 = "O"

        self.enterButton1.setEnabled(False)
        self.enterButton2.setEnabled(False)
        self.startButton.setEnabled(False)
        self.loadButton1.setEnabled(False)
        self.loadButton2.setEnabled(False)
        self.enterButton1.setEnabled(False)
        self.enterButton1.setEnabled(False)
        self.inputAlias1.setEnabled(False)
        self.inputAlias2.setEnabled(False)

    def switchPlayer(self):
        self.currentPlayer = "O" if self.currentPlayer == "X" else "X"

    def MakeNextFieldActive(self, row, column):
        if self.SmallFields[row][column].winner is None and not self.CheckIfFieldFull(self.SmallFields[row][column]):
            self.activeField = (row, column)
        else:
            self.activeField = None
        self.UpdateActiveFields()

    def UpdateActiveFields(self):
        if self.activeField:
            for i in range(3):
                for j in range(3):
                    if (i, j) == self.activeField:
                        self.SmallFields[i][j].enableField()
                    else:
                        self.SmallFields[i][j].disableField()
        else:
            self.MakeAllFieldsActive()

    def CheckIfFieldFull(self, grid):
        for i in range(3):
            for j in range(3):
                if grid.buttons[i][j].text() == "":
                    return False
        return True
    
    def declareWinner(self, winner):
        msg = QMessageBox()
        msg.setText(f"Player {self.alias1 if winner == 'X' else self.alias2} wins!")
        msg.exec()
        self.resetGame()

    def resetGame(self):
        self.currentPlayer == "X"
        for row in self.SmallFields:
            for grid in row:
                grid.winButton.setVisible(False)
                for i in range(3):
                    for j in range(3):
                        grid.buttons[i][j].setVisible(True)
                        grid.buttons[i][j].setText("")
                        grid.buttons[i][j].setEnabled(True)
                grid.winner = None

        self.activeField = None
        self.MakeAllFieldsActive()
        self.MakeAllFieldsEnabled(False)
        self.enterButton1.setEnabled(True)
        self.enterButton2.setEnabled(True)
        self.startButton.setEnabled(True)
        self.loadButton1.setEnabled(True)
        self.loadButton2.setEnabled(True)
        self.enterButton1.setEnabled(True)
        self.enterButton1.setEnabled(True)
        self.inputAlias1.setEnabled(True)
        self.inputAlias2.setEnabled(True)
        wnd.showMaximized()

    def checkOverallWinner(self):
        for i in range(3):
            if self.SmallFields[i][0].winner == self.SmallFields[i][1].winner == self.SmallFields[i][2].winner and self.SmallFields[i][0].winner is not None:
                self.declareWinner(self.SmallFields[i][0].winner)
                return
            if self.SmallFields[0][i].winner == self.SmallFields[1][i].winner == self.SmallFields[2][i].winner and self.SmallFields[0][i].winner is not None:
                self.declareWinner(self.SmallFields[i][0].winner)
                return
        if self.SmallFields[0][0].winner == self.SmallFields[1][1].winner == self.SmallFields[2][2].winner and self.SmallFields[0][0].winner is not None:
            self.declareWinner(self.SmallFields[0][0].winner)
            return
        if self.SmallFields[0][2].winner == self.SmallFields[1][1].winner == self.SmallFields[2][0].winner and self.SmallFields[0][2].winner is not None:
            self.declareWinner(self.SmallFields[0][0].winner)
            return

    def changeXColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.colors['X'] = color.name()

    def changeOColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.colors['O'] = color.name()

    def Surrender(self):
        if self.currentPlayer == "X":
            msg = QMessageBox()
            msg.setText(f"Player {self.alias2} wins!")
            msg.exec()
            self.resetGame()
        else:
            msg = QMessageBox()
            msg.setText(f"Player {self.alias1} wins!")
            msg.exec()
            self.resetGame()
    
    def checkOverallTie(self):
        for i in range(3):
            for j in range (3):
                if self.CheckIfFieldFull(self.SmallFields[i][j]) and not self.checkOverallWinner():
                    msg = QMessageBox()
                    msg.setText(f"Noone wins but both of you have tried, well played!")
                    msg.exec()
                    self.resetGame()

    def saveGame(self, grid):
        dataToSave = {
            'firstPlayerName': self.alias1,
            'secondPlayerName': self.alias2,
            'currentPlayer': self.currentPlayer,
            'colors': self.colors,
            'activeField': self.activeField,
            'state': self.updatingAndStoringStateOfGame(grid),
        }
        with open(file, 'w') as file:
            json.dump(dataToSave, file, indent=2)

    def updatingAndStoringStateOfGame(self, grid):
        return {
            'winner': self.SmallFields.winner,
            'winButton': grid.winButton.text(),
            'allButtons': self.updatingButtonsInField(),
        }
    
    def updatingButtonsInField(self):
        for buttons in row:
            for row in self.SmallFields.buttons:
                return buttons.text()
        for self.SmallFields in row:
            return self.SmallFields.winner

    def loadGame(self, file):   
        self.resetGame()
        with open(file, 'w') as file:
            dataToSave = json.load(file)
            self.alias1 = dataToSave['firstPlayerName']
            self.alias2 = dataToSave['secondPlayerName']
            self.currentPlayer = dataToSave['currentPlayer']
            self.activeField = dataToSave['activeField']
            self.colors = dataToSave['colors']
            self.enterButton1.setEnabled(False)
            self.enterButton2.setEnabled(False)
            self.startButton.setEnabled(False)
            self.loadButton1.setEnabled(False)
            self.loadButton2.setEnabled(False)
            self.enterButton1.setEnabled(False)
            self.enterButton1.setEnabled(False)
            self.inputAlias1.setEnabled(False)
            self.inputAlias2.setEnabled(False)
            self.UpdateActiveFields()
            self.MakeAllFieldsEnabled(True)
            self.MakeNextFieldActive(self.activeField[0], self.activeField[1])
            self.XColor = dataToSave['colors']['X']
            self.OColor = dataToSave['colors']['O']
            for z in range(3):
                for x in range(3):
                    for f9 in range (3):
                        for c in range (3):
                            self.SmallFields[z][x].buttons[f9][c].setText(dataToSave['state'][z][x]['allButtons'][f9][c])
                            if self.SmallFields[z][x].buttons[f9][c] == "X":
                                self.SmallFields[z][x].buttons[f9][c].setStyleSheet(f"colors: {self.XColor}; font-size: 35px;") 
                            else:
                                self.SmallFields[z][x].buttons[f9][c].setStyleSheet(f"colors: {self.OColor}; font-size: 35px;")
            for z in range(3):
                for x in range(3):
                    self.SmallFields[z][x].winner = dataToSave['state'][z][x]['winner']
                    self.SmallFields[x][x].winButton = dataToSave['state'][z][x]['winButton']
            for z in range(3):
                for x in range(3):
                    if self.SmallFields[z][x].winButton == "X" or self.SmallFields[z][x].winButton == "O":
                        self.SmallFields[z][x].winButton.setEnabled(False)
                        self.SmallFields[z][x].winButton.setVisible(True)
                        for f9 in range(3):
                            for c in range(3):
                                self.SmallFields[z][x].buttons[f9][c].setVisible(False)
                                self.SmallFields[z][x].buttons[f9][c].setEnabled(False)





app = QApplication(sys.argv)
wnd = Window()
wnd.showMaximized()
sys.exit(app.exec())

