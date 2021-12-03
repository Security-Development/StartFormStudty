import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QPushButton,QDesktopWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, Qt, QRect

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(600, 200)
        self.setStyleSheet("background-color: #f7f6f2")
        self.setWindowIcon(QtGui.QIcon('main.png'))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Game")

        self.window()
        self.start()
        self.text()
        self.center()
        self.quit()

    def window(self):
        label = QLabel("Chat Game", self)
        label.resize(600, 30)
        label.setFont(QtGui.QFont("궁서체",10))
        label.setStyleSheet("background-color: #0387fe; color: white; padding: 5px")

    def center(self):
        self.frameGeometry().moveCenter(QDesktopWidget().availableGeometry().center())

    def start(self):
        button = QPushButton("Start Game", self)
        button.resize(100, 50)
        button.move(100, 100)
        button.setFont(QtGui.QFont("궁서체",10))
        button.setStyleSheet("background-color: #0387fe; border: none; color: white")

    def text(self):
        label = QLabel("You want [ Play Game ]?", self)
        label.setStyleSheet("color: #0387fe;")
        label.setToolTip("Start the game")
        label.move(200,70)
        label.setFont(QtGui.QFont("궁서체",10))
        
        
    def quit(self):
        button = QPushButton("Quit", self)
        button.resize(100, 50)
        button.clicked.connect(self.closeEvent)
        button.move(400, 100)
        button.setToolTip("Close the window")
        button.setFont(QtGui.QFont("궁서체",10))
        button.setStyleSheet("background-color: #0387fe; border: none; color: white;")

    def closeEvent(self):
        sys.exit(0)
        
app = QApplication(sys.argv)
a = Main()
a.show()
sys.exit(app.exec_())
