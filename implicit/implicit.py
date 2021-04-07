import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from implicit_formula import *
from ExtractingData import *


qtCreatorFile = "implicit.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Implicit Options Calculator")

        #This line calls the extract function which fills in the historical data
        self.InputExtract.clicked.connect(self.Extract)
        
        #This line calls the extract function which fills in the historical data
        self.InputReset.clicked.connect(self.clearall)

        #This line calls the extract function which fills in the historical data
        self.InputCalculate.clicked.connect(self.VCalculate)


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
        self.InputStepsM.setText('')
        self.OutputText.setText('')


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
    
    def check(self):
        call = 1
        if self.InputCallButton.isChecked():
            call = 1
            print('call is check')
        if self.InputPutButton.isChecked():
            call = 0
            print('put is checked')

        return call

    def VCalculate(self,):
        S=float(self.InputStockPrice.text())
        K=float(self.InputStrikePrice.text())
        r=float(self.InputInterestRate.text())
        q=float(self.InputYieldRate.text())
        T=float(self.InputTimePeriod.text())
        sigma=float(self.InputSigma.text())
        N=int(self.InputStepsN.text())
        M = int(self.InputStepsM.text())
        call = self.check()

        #calculate the trinomial tree and return that value in the UI
        result = round(Implicit(S, K, r, q, T, sigma, M, N, call),2)
        self.OutputText.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())