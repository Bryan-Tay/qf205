import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton
from trinomial import *

qtCreatorFile = "Options.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        
        self.ExtractD.clicked.connect(self.Extract)
        self.CalculateV.clicked.connect(self.VCalculate)
        
    def Extract(self,):
        ticker=self.TickerLine.text()
        result1=stock_price(ticker)
        result2=rf_rate()
        result3=sd(ticker)
        result4=dividend_yield(ticker)
        self.SLine.setText(str(round(result1,10)))
        self.rLine.setText(str(round(result2,10)))
        self.SigmaLine.setText(str(round(result3,10)))
        self.qLine.setText(str(round(result4,10)))
    
    def VCalculate(self,):
        S=float(self.SLine.text())
        K=float(self.KLine.text())
        r=float(self.rLine.text())
        q=float(self.qLine.text())
        T=float(self.TLine.text())
        sigma=float(self.SigmaLine.text())
        M=int(self.MLine.text())
        N=int(self.NLine.text())
        call=0

        if self.CallButton.isChecked():
            call=1
        else:
            call=0
        
        if self.ImplicitButton.isChecked():
            result = Implicit(S,K,r,q,T,sigma,M,N,call)
            
        elif self.ExplicitButton.isChecked():
            result = Explicit(S,K,r,q,T,sigma,M,N,call)
            
        self.VLine.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())