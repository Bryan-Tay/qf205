# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Options.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName("Options")
        Options.resize(800, 670)
        self.centralwidget = QtWidgets.QWidget(Options)
        self.centralwidget.setObjectName("centralwidget")
        self.StockPrice = QtWidgets.QLabel(self.centralwidget)
        self.StockPrice.setGeometry(QtCore.QRect(10, 222, 251, 31))
        self.StockPrice.setObjectName("StockPrice")
        self.Sigma = QtWidgets.QLabel(self.centralwidget)
        self.Sigma.setGeometry(QtCore.QRect(10, 367, 181, 31))
        self.Sigma.setObjectName("Sigma")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(-10, 1, 801, 111))
        self.Title.setObjectName("Title")
        self.Increments = QtWidgets.QLabel(self.centralwidget)
        self.Increments.setGeometry(QtCore.QRect(10, 396, 268, 31))
        self.Increments.setObjectName("Increments")
        self.YieldRate = QtWidgets.QLabel(self.centralwidget)
        self.YieldRate.setGeometry(QtCore.QRect(10, 309, 201, 31))
        self.YieldRate.setObjectName("YieldRate")
        self.MethodLine = QtWidgets.QLabel(self.centralwidget)
        self.MethodLine.setGeometry(QtCore.QRect(10, 193, 151, 23))
        self.MethodLine.setObjectName("MethodLine")
        self.Periods = QtWidgets.QLabel(self.centralwidget)
        self.Periods.setGeometry(QtCore.QRect(10, 425, 209, 31))
        self.Periods.setObjectName("Periods")
        self.StrikePrice = QtWidgets.QLabel(self.centralwidget)
        self.StrikePrice.setGeometry(QtCore.QRect(10, 251, 231, 31))
        self.StrikePrice.setObjectName("StrikePrice")
        self.TimeEnd = QtWidgets.QLabel(self.centralwidget)
        self.TimeEnd.setGeometry(QtCore.QRect(10, 338, 221, 31))
        self.TimeEnd.setObjectName("TimeEnd")
        self.CallPrice = QtWidgets.QLabel(self.centralwidget)
        self.CallPrice.setGeometry(QtCore.QRect(10, 473, 201, 41))
        self.CallPrice.setObjectName("CallPrice")
        self.TickerLabel = QtWidgets.QLabel(self.centralwidget)
        self.TickerLabel.setGeometry(QtCore.QRect(10, 136, 141, 31))
        self.TickerLabel.setObjectName("TickerLabel")
        self.Rate = QtWidgets.QLabel(self.centralwidget)
        self.Rate.setGeometry(QtCore.QRect(10, 280, 211, 31))
        self.Rate.setObjectName("Rate")
        self.SLine = QtWidgets.QLineEdit(self.centralwidget)
        self.SLine.setGeometry(QtCore.QRect(887, 546, 133, 20))
        self.SLine.setObjectName("SLine")
        self.PutButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PutButton.setGeometry(QtCore.QRect(960, 490, 39, 17))
        self.PutButton.setObjectName("PutButton")
        self.Increments_2 = QtWidgets.QLabel(self.centralwidget)
        self.Increments_2.setGeometry(QtCore.QRect(500, 719, 411, 23))
        self.Increments_2.setObjectName("Increments_2")
        self.TickerLine = QtWidgets.QLineEdit(self.centralwidget)
        self.TickerLine.setGeometry(QtCore.QRect(887, 430, 133, 20))
        self.TickerLine.setObjectName("TickerLine")
        self.qLine = QtWidgets.QLineEdit(self.centralwidget)
        self.qLine.setGeometry(QtCore.QRect(887, 633, 133, 20))
        self.qLine.setObjectName("qLine")
        self.MLine = QtWidgets.QLineEdit(self.centralwidget)
        self.MLine.setGeometry(QtCore.QRect(887, 720, 133, 20))
        self.MLine.setObjectName("MLine")
        self.ExplicitButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ExplicitButton.setGeometry(QtCore.QRect(898, 519, 56, 17))
        self.ExplicitButton.setObjectName("ExplicitButton")
        self.VLine = QtWidgets.QLineEdit(self.centralwidget)
        self.VLine.setGeometry(QtCore.QRect(887, 807, 133, 20))
        self.VLine.setObjectName("VLine")
        self.ImplicitButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ImplicitButton.setGeometry(QtCore.QRect(960, 519, 56, 17))
        self.ImplicitButton.setObjectName("ImplicitButton")
        self.NLine = QtWidgets.QLineEdit(self.centralwidget)
        self.NLine.setGeometry(QtCore.QRect(887, 749, 133, 20))
        self.NLine.setObjectName("NLine")
        self.ExtractD = QtWidgets.QPushButton(self.centralwidget)
        self.ExtractD.setGeometry(QtCore.QRect(900, 458, 111, 23))
        self.ExtractD.setObjectName("ExtractD")
        self.SigmaLine = QtWidgets.QLineEdit(self.centralwidget)
        self.SigmaLine.setGeometry(QtCore.QRect(887, 691, 133, 20))
        self.SigmaLine.setObjectName("SigmaLine")
        self.CallButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CallButton.setGeometry(QtCore.QRect(898, 490, 40, 17))
        self.CallButton.setObjectName("CallButton")
        self.TLine = QtWidgets.QLineEdit(self.centralwidget)
        self.TLine.setGeometry(QtCore.QRect(887, 662, 133, 20))
        self.TLine.setObjectName("TLine")
        self.rLine = QtWidgets.QLineEdit(self.centralwidget)
        self.rLine.setGeometry(QtCore.QRect(887, 604, 133, 20))
        self.rLine.setObjectName("rLine")
        self.KLine = QtWidgets.QLineEdit(self.centralwidget)
        self.KLine.setGeometry(QtCore.QRect(887, 575, 133, 20))
        self.KLine.setObjectName("KLine")
        self.CalculateV = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateV.setGeometry(QtCore.QRect(900, 777, 111, 23))
        self.CalculateV.setObjectName("CalculateV")
        self.SLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.SLine_2.setGeometry(QtCore.QRect(1027, 506, 133, 20))
        self.SLine_2.setObjectName("SLine_2")
        self.MLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.MLine_2.setGeometry(QtCore.QRect(1027, 680, 133, 20))
        self.MLine_2.setObjectName("MLine_2")
        self.ExplicitButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.ExplicitButton_2.setGeometry(QtCore.QRect(1038, 479, 56, 17))
        self.ExplicitButton_2.setObjectName("ExplicitButton_2")
        self.VLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.VLine_2.setGeometry(QtCore.QRect(1027, 767, 133, 20))
        self.VLine_2.setObjectName("VLine_2")
        self.KLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.KLine_2.setGeometry(QtCore.QRect(1027, 535, 133, 20))
        self.KLine_2.setObjectName("KLine_2")
        self.PutButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.PutButton_2.setGeometry(QtCore.QRect(1100, 450, 39, 17))
        self.PutButton_2.setObjectName("PutButton_2")
        self.TLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.TLine_2.setGeometry(QtCore.QRect(1027, 622, 133, 20))
        self.TLine_2.setObjectName("TLine_2")
        self.NLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.NLine_2.setGeometry(QtCore.QRect(1027, 709, 133, 20))
        self.NLine_2.setObjectName("NLine_2")
        self.rLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.rLine_2.setGeometry(QtCore.QRect(1027, 564, 133, 20))
        self.rLine_2.setObjectName("rLine_2")
        self.TickerLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.TickerLine_2.setGeometry(QtCore.QRect(1027, 390, 133, 20))
        self.TickerLine_2.setObjectName("TickerLine_2")
        self.CalculateV_2 = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateV_2.setGeometry(QtCore.QRect(1040, 737, 111, 23))
        self.CalculateV_2.setObjectName("CalculateV_2")
        self.Increments_3 = QtWidgets.QLabel(self.centralwidget)
        self.Increments_3.setGeometry(QtCore.QRect(640, 679, 411, 23))
        self.Increments_3.setObjectName("Increments_3")
        self.CallButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.CallButton_2.setGeometry(QtCore.QRect(1038, 450, 40, 17))
        self.CallButton_2.setObjectName("CallButton_2")
        self.qLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.qLine_2.setGeometry(QtCore.QRect(1027, 593, 133, 20))
        self.qLine_2.setObjectName("qLine_2")
        self.ExtractD_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ExtractD_2.setGeometry(QtCore.QRect(1040, 418, 111, 23))
        self.ExtractD_2.setObjectName("ExtractD_2")
        self.SigmaLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.SigmaLine_2.setGeometry(QtCore.QRect(1027, 651, 133, 20))
        self.SigmaLine_2.setObjectName("SigmaLine_2")
        self.ImplicitButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.ImplicitButton_2.setGeometry(QtCore.QRect(1100, 479, 56, 17))
        self.ImplicitButton_2.setObjectName("ImplicitButton_2")
        self.SLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.SLine_3.setGeometry(QtCore.QRect(897, 566, 133, 20))
        self.SLine_3.setObjectName("SLine_3")
        self.PutButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.PutButton_3.setGeometry(QtCore.QRect(970, 510, 39, 17))
        self.PutButton_3.setObjectName("PutButton_3")
        self.Increments_4 = QtWidgets.QLabel(self.centralwidget)
        self.Increments_4.setGeometry(QtCore.QRect(510, 739, 411, 23))
        self.Increments_4.setObjectName("Increments_4")
        self.TickerLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.TickerLine_3.setGeometry(QtCore.QRect(897, 450, 133, 20))
        self.TickerLine_3.setObjectName("TickerLine_3")
        self.qLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.qLine_3.setGeometry(QtCore.QRect(897, 653, 133, 20))
        self.qLine_3.setObjectName("qLine_3")
        self.MLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.MLine_3.setGeometry(QtCore.QRect(897, 740, 133, 20))
        self.MLine_3.setObjectName("MLine_3")
        self.ExplicitButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.ExplicitButton_3.setGeometry(QtCore.QRect(908, 539, 56, 17))
        self.ExplicitButton_3.setObjectName("ExplicitButton_3")
        self.VLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.VLine_3.setGeometry(QtCore.QRect(897, 827, 133, 20))
        self.VLine_3.setObjectName("VLine_3")
        self.ImplicitButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.ImplicitButton_3.setGeometry(QtCore.QRect(970, 539, 56, 17))
        self.ImplicitButton_3.setObjectName("ImplicitButton_3")
        self.NLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.NLine_3.setGeometry(QtCore.QRect(897, 769, 133, 20))
        self.NLine_3.setObjectName("NLine_3")
        self.ExtractD_3 = QtWidgets.QPushButton(self.centralwidget)
        self.ExtractD_3.setGeometry(QtCore.QRect(910, 478, 111, 23))
        self.ExtractD_3.setObjectName("ExtractD_3")
        self.SigmaLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.SigmaLine_3.setGeometry(QtCore.QRect(897, 711, 133, 20))
        self.SigmaLine_3.setObjectName("SigmaLine_3")
        self.CallButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.CallButton_3.setGeometry(QtCore.QRect(908, 510, 40, 17))
        self.CallButton_3.setObjectName("CallButton_3")
        self.TLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.TLine_3.setGeometry(QtCore.QRect(897, 682, 133, 20))
        self.TLine_3.setObjectName("TLine_3")
        self.rLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.rLine_3.setGeometry(QtCore.QRect(897, 624, 133, 20))
        self.rLine_3.setObjectName("rLine_3")
        self.KLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.KLine_3.setGeometry(QtCore.QRect(897, 595, 133, 20))
        self.KLine_3.setObjectName("KLine_3")
        self.CalculateV_3 = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateV_3.setGeometry(QtCore.QRect(910, 797, 111, 23))
        self.CalculateV_3.setObjectName("CalculateV_3")
        self.SLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.SLine_4.setGeometry(QtCore.QRect(297, 239, 133, 20))
        self.SLine_4.setObjectName("SLine_4")
        self.TickerLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.TickerLine_4.setGeometry(QtCore.QRect(297, 123, 133, 20))
        self.TickerLine_4.setObjectName("TickerLine_4")
        self.MLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.MLine_4.setGeometry(QtCore.QRect(297, 413, 133, 20))
        self.MLine_4.setObjectName("MLine_4")
        self.qLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.qLine_4.setGeometry(QtCore.QRect(297, 326, 133, 20))
        self.qLine_4.setObjectName("qLine_4")
        self.VLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.VLine_4.setGeometry(QtCore.QRect(297, 500, 133, 20))
        self.VLine_4.setObjectName("VLine_4")
        self.ExplicitButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.ExplicitButton_4.setGeometry(QtCore.QRect(308, 212, 56, 17))
        self.ExplicitButton_4.setObjectName("ExplicitButton_4")
        self.NLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.NLine_4.setGeometry(QtCore.QRect(297, 442, 133, 20))
        self.NLine_4.setObjectName("NLine_4")
        self.ImplicitButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.ImplicitButton_4.setGeometry(QtCore.QRect(370, 212, 56, 17))
        self.ImplicitButton_4.setObjectName("ImplicitButton_4")
        self.ExtractD_4 = QtWidgets.QPushButton(self.centralwidget)
        self.ExtractD_4.setGeometry(QtCore.QRect(310, 151, 111, 23))
        self.ExtractD_4.setObjectName("ExtractD_4")
        self.SigmaLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.SigmaLine_4.setGeometry(QtCore.QRect(297, 384, 133, 20))
        self.SigmaLine_4.setObjectName("SigmaLine_4")
        self.TLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.TLine_4.setGeometry(QtCore.QRect(297, 355, 133, 20))
        self.TLine_4.setObjectName("TLine_4")
        self.rLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.rLine_4.setGeometry(QtCore.QRect(297, 297, 133, 20))
        self.rLine_4.setObjectName("rLine_4")
        self.KLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.KLine_4.setGeometry(QtCore.QRect(297, 268, 133, 20))
        self.KLine_4.setObjectName("KLine_4")
        self.CalculateV_4 = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateV_4.setGeometry(QtCore.QRect(310, 470, 111, 23))
        self.CalculateV_4.setObjectName("CalculateV_4")
        Options.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Options)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Options.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Options)
        self.statusbar.setObjectName("statusbar")
        Options.setStatusBar(self.statusbar)

        self.retranslateUi(Options)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        _translate = QtCore.QCoreApplication.translate
        Options.setWindowTitle(_translate("Options", "MainWindow"))
        self.StockPrice.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Stock Price (S)</span></p></body></html>"))
        self.Sigma.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Sigma (σ)</span></p></body></html>"))
        self.Title.setText(_translate("Options", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline;\">Option Price Calculator</span></p></body></html>"))
        self.Increments.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">No. of Price Movements (M)</span></p></body></html>"))
        self.YieldRate.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Yield Rate (q)</span></p></body></html>"))
        self.MethodLine.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Method</span></p></body></html>"))
        self.Periods.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">No. of Time Steps (N)</span></p></body></html>"))
        self.StrikePrice.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Strike Price (K)</span></p></body></html>"))
        self.TimeEnd.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Time period (T)</span></p></body></html>"))
        self.CallPrice.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Option Price</span></p></body></html>"))
        self.TickerLabel.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Ticker</span></p></body></html>"))
        self.Rate.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Interest Rate (r)</span></p></body></html>"))
        self.PutButton.setText(_translate("Options", "Put"))
        self.Increments_2.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">No. of Price Movements (M)</span></p></body></html>"))
        self.ExplicitButton.setText(_translate("Options", "Explicit"))
        self.ImplicitButton.setText(_translate("Options", "Implicit"))
        self.ExtractD.setText(_translate("Options", "Extract Data"))
        self.CallButton.setText(_translate("Options", "Call"))
        self.CalculateV.setText(_translate("Options", "Calculate V"))
        self.ExplicitButton_2.setText(_translate("Options", "Explicit"))
        self.PutButton_2.setText(_translate("Options", "Put"))
        self.CalculateV_2.setText(_translate("Options", "Calculate V"))
        self.Increments_3.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">No. of Price Movements (M)</span></p></body></html>"))
        self.CallButton_2.setText(_translate("Options", "Call"))
        self.ExtractD_2.setText(_translate("Options", "Extract Data"))
        self.ImplicitButton_2.setText(_translate("Options", "Implicit"))
        self.PutButton_3.setText(_translate("Options", "Put"))
        self.Increments_4.setText(_translate("Options", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">No. of Price Movements (M)</span></p></body></html>"))
        self.ExplicitButton_3.setText(_translate("Options", "Explicit"))
        self.ImplicitButton_3.setText(_translate("Options", "Implicit"))
        self.ExtractD_3.setText(_translate("Options", "Extract Data"))
        self.CallButton_3.setText(_translate("Options", "Call"))
        self.CalculateV_3.setText(_translate("Options", "Calculate V"))
        self.ExplicitButton_4.setText(_translate("Options", "Explicit"))
        self.ImplicitButton_4.setText(_translate("Options", "Implicit"))
        self.ExtractD_4.setText(_translate("Options", "Extract Data"))
        self.CalculateV_4.setText(_translate("Options", "Calculate V"))
