from PyQt5 import QtWidgets, QtGui
import design
import sys
from functions import *

spm = SplashManager()
spm.load_splashes()
dm = DataManager()
dm.load_data()

can = 'QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;} QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} QPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}'
cant = 'QPushButton {color: #BF3737 ; background-color: #2D2D2D; border: none;} QPushButton:hover {color: #DA3C3C ; background-color: #3A3A39; border: none;} QPushButton:pressed {color: #F54343 ; background-color: #474746; border: none;}'

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = App()
window.setWindowTitle('{gamename} [{version}] by {author}. ({splash})'.replace('{splash}', spm.get()).replace('{gamename}', dm.gamename).replace('{author}', dm.author).replace('{version}', dm.version))
# window.setWindowIcon(QtGui.QIcon('icon.png'))
window.show()

# pyinstaller start.py -F //to make EXE
# pyuic5 design.ui -o design.py //to import PyQt5
# #######################################################################

game = Game()
def update():
    window.clicks.setText(str(game.clicks))
    if game.level_cost > game.clicks:
        window.upgrade_button.setStyleSheet(cant)
    else:
        window.upgrade_button.setStyleSheet(can)

def click():
    game.add_click()
    update()

def upgrade():
    game.level_up()
    update()

def save():
    game.save()
    update()

def load():
    game.load()
    update()


window.upgrade_button.clicked.connect(upgrade)
window.click_button.clicked.connect(click)
window.save_button.clicked.connect(save)
window.load_button.clicked.connect(load)

load()

# #######################################################################
app.exec_()