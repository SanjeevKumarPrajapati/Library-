# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'issue.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_issue(object):
    def setupUi(self, issue):
        issue.setObjectName("issue")
        issue.resize(461, 331)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        issue.setFont(font)
        issue.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(issue)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 90, 201, 71))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semibold")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 175, 126, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        issue.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(issue)
        self.statusbar.setObjectName("statusbar")
        issue.setStatusBar(self.statusbar)

        self.retranslateUi(issue)
        QtCore.QMetaObject.connectSlotsByName(issue)

    def retranslateUi(self, issue):
        _translate = QtCore.QCoreApplication.translate
        issue.setWindowTitle(_translate("issue", "MainWindow"))
        self.label.setText(_translate("issue", "Name"))
        self.label_2.setText(_translate("issue", "Book No."))
        self.pushButton_2.setText(_translate("issue", "Back"))
        self.pushButton.setText(_translate("issue", "Issue Book"))
        self.label_3.setText(_translate("issue", "Issue Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    issue = QtWidgets.QMainWindow()
    ui = Ui_issue()
    ui.setupUi(issue)
    issue.show()
    sys.exit(app.exec_())
