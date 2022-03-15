from curses import window
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('todo.ui', self)
        self.show()
        
        self.addButton.clicked.connect(self.add)
        
    def add(self):    
        print("Add Clicked")
        
app = QtWidgets.QApplication(sys.argv)
window = Ui()
sys.exit(app.exec_())