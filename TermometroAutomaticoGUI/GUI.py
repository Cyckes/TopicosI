# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 654)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pngegg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 113, 168);")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 40, 81, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 220, 111, 31))
        self.label_2.setObjectName("label_2")
        self.txtSalida = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSalida.setGeometry(QtCore.QRect(70, 270, 331, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtSalida.setFont(font)
        self.txtSalida.setStyleSheet("background-color: rgb(255, 245, 238);")
        self.txtSalida.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtSalida.setReadOnly(True)
        self.txtSalida.setObjectName("txtSalida")
        self.txtEntrada = QtWidgets.QTextEdit(self.centralwidget)
        self.txtEntrada.setGeometry(QtCore.QRect(130, 100, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtEntrada.setFont(font)
        self.txtEntrada.setStyleSheet("background-color: rgb(255, 245, 238);")
        self.txtEntrada.setObjectName("txtEntrada")
        self.botonEjecutar = QtWidgets.QPushButton(self.centralwidget)
        self.botonEjecutar.setGeometry(QtCore.QRect(180, 170, 97, 29))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.botonEjecutar.setFont(font)
        self.botonEjecutar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botonEjecutar.setObjectName("botonEjecutar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 580, 59, 17))
        self.label_3.setObjectName("label_3")
        self.labelEstado = QtWidgets.QLabel(self.centralwidget)
        self.labelEstado.setGeometry(QtCore.QRect(190, 560, 181, 61))
        self.labelEstado.setFrameShape(QtWidgets.QFrame.Box)
        self.labelEstado.setScaledContents(True)
        self.labelEstado.setObjectName("labelEstado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Medidor de Temperatura Automático"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#f5973d;\">Entrada</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#f5973d;\">Salida</span></p></body></html>"))
        self.txtEntrada.setToolTip(_translate("MainWindow", "Comando: \"distancia NÚMERO\""))
        self.botonEjecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Estado</span></p></body></html>"))
        self.labelEstado.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
