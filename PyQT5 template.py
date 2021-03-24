import sys
from PyQt5.QtWidgets import QMainWindow, QApplication # more widgets
from PyQt5 import uic
# more imports
import pandas as pd
import numpy as np


qtCreatorFile = "FromQtDesigner.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # more initialzation

    def initUI(self):
        self.resize(250, 150)
        self.move(300,300)
        self.setWindowTitle('Simple')


    # more functions/methods        
    
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=Main()
    main.show()
    sys.exit(app.exec_())