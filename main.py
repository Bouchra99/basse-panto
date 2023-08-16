# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import logo_rc
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 768)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.compositionLabel = QtWidgets.QLabel(self.centralwidget)
        self.compositionLabel.setGeometry(QtCore.QRect(90, 130, 171, 31))
        self.compositionLabel.setStyleSheet("font-size:18px;\n"
"")
        self.compositionLabel.setObjectName("compositionLabel")
        self.vitesseInitLabel = QtWidgets.QLabel(self.centralwidget)
        self.vitesseInitLabel.setGeometry(QtCore.QRect(90, 180, 171, 31))
        self.vitesseInitLabel.setStyleSheet("font-size:18px;")
        self.vitesseInitLabel.setObjectName("vitesseInitLabel")
        self.PkInitLabel = QtWidgets.QLabel(self.centralwidget)
        self.PkInitLabel.setGeometry(QtCore.QRect(90, 230, 171, 31))
        self.PkInitLabel.setStyleSheet("font-size:18px;")
        self.PkInitLabel.setObjectName("PkInitLabel")
        self.PkFinLabel = QtWidgets.QLabel(self.centralwidget)
        self.PkFinLabel.setGeometry(QtCore.QRect(90, 280, 161, 31))
        self.PkFinLabel.setStyleSheet("font-size:18px;")
        self.PkFinLabel.setObjectName("PkFinLabel")
        self.declivitaLabel = QtWidgets.QLabel(self.centralwidget)
        self.declivitaLabel.setGeometry(QtCore.QRect(90, 330, 161, 31))
        self.declivitaLabel.setStyleSheet("font-size:18px;")
        self.declivitaLabel.setObjectName("declivitaLabel")
        self.resultBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resultBtn.setGeometry(QtCore.QRect(180, 460, 201, 51))
        self.resultBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultBtn.setStyleSheet("border-radius:2px;\n"
"font-size:20px;\n"
"background-color:rgb(221, 73, 0);\n"
"color:rgb(255,255,255) ;\n"
"font-weight:bold;")
        self.resultBtn.setObjectName("resultBtn")
        self.compositionInput = QtWidgets.QLineEdit(self.centralwidget)
        self.compositionInput.setGeometry(QtCore.QRect(270, 129, 221, 31))
        self.compositionInput.setStyleSheet("border-radius:2px;\n"
"border : 1px solid rgb(161, 161, 161);\n"
"font-size:18px;\n"
"padding-left:5px;")
        self.compositionInput.setObjectName("compositionInput")
        self.vitesseInitInput = QtWidgets.QLineEdit(self.centralwidget)
        self.vitesseInitInput.setGeometry(QtCore.QRect(270, 180, 221, 31))
        self.vitesseInitInput.setStyleSheet("border-radius:2px;\n"
"border : 1px solid rgb(161, 161, 161);\n"
"font-size:18px;\n"
"padding-left:5px;")
        self.vitesseInitInput.setObjectName("vitesseInitInput")
        self.pkInitInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pkInitInput.setGeometry(QtCore.QRect(270, 230, 221, 31))
        self.pkInitInput.setStyleSheet("border-radius:2px;\n"
"border : 1px solid rgb(161, 161, 161);\n"
"font-size:18px;\n"
"padding-left:5px;")
        self.pkInitInput.setObjectName("pkInitInput")
        self.pkFinInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pkFinInput.setGeometry(QtCore.QRect(270, 280, 221, 31))
        self.pkFinInput.setStyleSheet("border-radius:2px;\n"
"border : 1px solid rgb(161, 161, 161);\n"
"font-size:18px;\n"
"padding-left:5px;")
        self.pkFinInput.setObjectName("pkFinInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 151, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/oncf.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.decliviteInput = QtWidgets.QLineEdit(self.centralwidget)
        self.decliviteInput.setGeometry(QtCore.QRect(270, 330, 221, 31))
        self.decliviteInput.setStyleSheet("border-radius:2px;\n"
"border : 1px solid rgb(161, 161, 161);\n"
"font-size:18px;\n"
"padding-left:5px;")
        self.decliviteInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.decliviteInput.setText("")
        self.decliviteInput.setObjectName("decliviteInput")
        self.timeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.timeInput.setGeometry(QtCore.QRect(270, 379, 221, 31))
        self.timeInput.setStyleSheet("border-radius:2px;\n"
"border : 1px solid rgb(161, 161, 161);\n"
"font-size:18px;\n"
"padding-left:5px;")
        self.timeInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.timeInput.setText("")
        self.timeInput.setObjectName("timeInput")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(90, 380, 171, 31))
        self.timeLabel.setStyleSheet("font-size:18px;")
        self.timeLabel.setObjectName("timeLabel")

        self.resultTable = QtWidgets.QTableWidget(self.centralwidget)
        self.resultTable.setGeometry(QtCore.QRect(50, 560, 471, 90))
        self.resultTable.setStyleSheet("border-radius : 5px;\n"
"font-size:18px;")
        self.resultTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.resultTable.setRowCount(2)
 
        self.resultTable.verticalHeader().setVisible(True)
        self.resultTable.horizontalHeader().setVisible(False)
        self.resultTable.setVerticalHeaderLabels(["Vitesse (km/h)", "Distance (m)"])

      

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 385, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Panto baisse TGV"))
        self.compositionLabel.setText(_translate("MainWindow", "Composition TGV"))
        self.vitesseInitLabel.setText(_translate("MainWindow", "Vitesse Initiale"))
        self.PkInitLabel.setText(_translate("MainWindow", "PK Initial"))
        self.PkFinLabel.setText(_translate("MainWindow", "PK Final"))
        self.declivitaLabel.setText(_translate("MainWindow", "Declivité"))
        self.resultBtn.setText(_translate("MainWindow", "Submit"))
        self.compositionInput.setPlaceholderText(_translate("MainWindow", "US | UM "))
        self.vitesseInitInput.setPlaceholderText(_translate("MainWindow", "km/h"))
        self.pkInitInput.setPlaceholderText(_translate("MainWindow", "m"))
        self.pkFinInput.setPlaceholderText(_translate("MainWindow", "m"))
        self.decliviteInput.setPlaceholderText(_translate("MainWindow", "mm/m"))
        self.timeInput.setPlaceholderText(_translate("MainWindow", "s"))
        self.timeLabel.setText(_translate("MainWindow", "Temps"))
    

    def onSubmit(self):
        r = 300  # Rayon de la courbe en m
        
       
        alpha = float(self.decliviteInput.text())
        
        temps = int(self.timeInput.text()) # nombre de seconde de mouvement 
        pkInit = int(self.pkInitInput.text()) 
        pkFinal = int(self.pkFinInput.text())
        # l = list(range(temps)) # unite de temps en s

        x0 = 0

        x= [x0] 
        xmax = abs(pkFinal  - pkInit)
        xw = [math.floor(x0)]
        
        v0 = float(self.vitesseInitInput.text())/3.6 # vitesse initial en km/h a l'instant du baisse du panto
        v=[v0]
        vkph = [math.floor(3.6*v0)]

        composition = self.compositionInput.text().upper()
        match composition :
            case "UM" : 
                r1=5.8
                r2=0.021
                r3=0.0000747
                m=900
            case "US" : 
                r1=2.9
                r2=0.0209
                r3=0.0000746
                m=450

        for i in range(temps-1):
             v=v+[v[i]-9.8*(math.sin(math.atan(alpha))+0.8/r) -r1/m-(r2/m)*v[i]-(r3/m)*v[i]*v[i]]
             x=x+[x[i]+v[i]+0.5*(-9.8*(math.sin(math.atan(alpha))+0.8/r) -r1/m-(r2/m)*v[i]-(r3/m)*v[i]*v[i])]
             if x[i]>xmax:
                break            #le prgramme arrete le calcul au PK de changement de R ou alpha
             xw=xw+[math.floor(x[i+1])]
             vkph=vkph+[math.floor(3.6*v[i+1])]


      

        time_values = list(range(temps-1))
        self.resultTable.setRowCount(3) 
        
        self.resultTable.setVerticalHeaderLabels(["Temps (s)","Vitesse (km/h)", "Distance (m)"])
        self.resultTable.setColumnCount(len(xw))
        for col, (c, x, t) in enumerate(zip(vkph, xw, time_values)):
            self.resultTable.setItem(0,col, QtWidgets.QTableWidgetItem(str(t)))
            self.resultTable.setItem(2,col, QtWidgets.QTableWidgetItem(str(x)))
            self.resultTable.setItem(1,col,  QtWidgets.QTableWidgetItem(str(c)))

        self.resultTable.resizeRowsToContents()

        plt.figure(figsize=(10, 6))
        
        plt.subplot(2, 1, 1)
        plt.plot(time_values[:len(vkph)], vkph, marker='o', linestyle='-', color='b')
        plt.xlabel('Temps (s)')
        plt.ylabel('Vitesse (km/h)')
        plt.title('Vitesse en fonction du temps')

        plt.subplot(2, 1, 2)
        plt.plot(time_values[:len(xw)], xw, marker='o', linestyle='-', color='r')
        plt.xlabel('Temps (s)')
        plt.ylabel('Distance (m)')
        plt.title('Distance parcourue en fonction du temps')

        plt.tight_layout()
        plt.show()
      
      





import matplotlib.pyplot as plt



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.resultBtn.clicked.connect(ui.onSubmit)
    MainWindow.show()
    sys.exit(app.exec_())



