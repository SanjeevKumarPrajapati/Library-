# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'return1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_return1(object):
    def setupUi(self, return1):
        return1.setObjectName("return1")
        return1.resize(465, 332)
        return1.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(return1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(130, 100, 201, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 180, 126, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semibold")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        return1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(return1)
        self.statusbar.setObjectName("statusbar")
        return1.setStatusBar(self.statusbar)

        self.retranslateUi(return1)
        QtCore.QMetaObject.connectSlotsByName(return1)

    def retranslateUi(self, return1):
        _translate = QtCore.QCoreApplication.translate
        return1.setWindowTitle(_translate("return1", "MainWindow"))
        self.label_3.setText(_translate("return1", "Return Book"))
        self.label.setText(_translate("return1", "Name"))
        self.label_2.setText(_translate("return1", "Book No."))
        self.pushButton.setText(_translate("return1", "Return Book"))
        self.pushButton_2.setText(_translate("return1", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    return1 = QtWidgets.QMainWindow()
    ui = Ui_return1()
    ui.setupUi(return1)
    return1.show()
    sys.exit(app.exec_())
