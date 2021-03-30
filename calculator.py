import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton
from trinomial import *
from ExtractingData import *
from MainWindow import Ui_MainWindow

import gui

qtCreatorFile = "calculator.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):        
        super().__init__()
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Options Calculator")
        # self.pushButton = QtWidgets.QPushButton(self.Implicit_Explicit)
        self.Trinomial.clicked.connect(self.hello)


    def page_update(self):
        index = self.ui.list

    

    def hello(self):
        print('Hello tab is clicked implicit')
        # self.Stack.setCurrentIndex(i)
        # self.check()
        print(self.setupUi.CurrentIndex())


    def check(self):
        if self.InputImplicitButton.isChecked():
            print('implicit')
        if self.InputExplicitButton.isChecked():
            print('explicit')

        self.testing()

    def testing(self):
        self.OutputText.setText('This is the output')


    def clearall(self):
        #this functions resets all the inputs for all the text box
        self.InputStockPrice.setText('')
        self.InputInterestRate.setText('')
        self.InputSigma.setText('')
        self.InputYieldRate.setText('')
        self.InputTicker.setText('')
        self.InputStepsN.setText('')
        self.InputTimePeriod.setText('')
        self.InputStrikePrice.setText('')



    # def initUI(self):
    def Extract(self,):
        ticker=self.InputTicker.text()
        input_stock_price = stock_price(ticker)
        input_interest_rate = rf_rate()
        input_sigma = sd(ticker)
        input_yield_rate = dividend_yield(ticker)
        self.InputStockPrice.setText(str(round(input_stock_price,10)))
        self.InputInterestRate.setText(str(round(input_interest_rate,10)))
        self.InputSigma.setText(str(round(input_sigma,10)))
        self.InputYieldRate.setText(str(round(input_yield_rate,10)))
    
    def VCalculate(self,):
        S=float(self.SLine_4.text())
        K=float(self.KLine_4.text())
        r=float(self.rLine_4.text())
        q=float(self.qLine_4.text())
        T=float(self.TLine_4.text())
        sigma=float(self.SigmaLine_4.text())
        M=int(self.MLine_4.text())
        N=int(self.NLine_4.text())
        call=0

        if self.CallButton.isChecked():
            call=1
        else:
            call=0
        
        if self.ImplicitButton_4.isChecked():
            print('implicit buttom working')
            result = trinomial_tree(S, K, r, q, T, sigma, N)
            
        elif self.ExplicitButton_4.isChecked():
            print("explicit button working")
            result = trinomial_tree(S, K, r, q, T, sigma, N)
            
        self.VLine.setText_4(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())