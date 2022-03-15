from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('todo.ui', self)
        self.show()
        
        self.addButton.clicked.connect(self.add)
        self.doneButton.clicked.connect(self.done)
        self.doneButton.clicked.connect(self.clear)
        
    def add(self):    
        
        if self.joblineEdit.text():
            strjob = self.joblineEdit.text()
            self.jobslistWidget.addItem(strjob)
            self.joblineEdit.setText("")
            self.joblineEdit.setFocus()

    def done(self):    
        
        clickedIndex = self.jobslistWidget.currentRow()
        self.jobslistWidget.takeItem(clickedIndex)
        
        
    def clear(self):
            
        
        
app = QtWidgets.QApplication(sys.argv)
window = Ui()
sys.exit(app.exec_())