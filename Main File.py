from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import sys
from welcome import Ui_Welcome
from registration import Ui_Registration
from faculty import Ui_faculty
from issue import Ui_issue
from add_book import Ui_add_book
from return1 import Ui_return1
listbook=[25678,78956,89563,89765,14233,65243]
dict={}
class welcome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Welcome()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.faculty)
        self.ui.pushButton_2.clicked.connect(self.registration)
    def faculty(self):
        self.st=faculty()
        self.st.show()
        self.hide()
    def registration(self):
        self.rg=registration()
        self.rg.show()
        self.hide()
class registration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Registration()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.registration)
        self.ui.pushButton_2.clicked.connect(self.back)
    def registration(self):
        name=self.ui.lineEdit.text()
        course=self.ui.lineEdit_2.text()
        branch=self.ui.lineEdit_3.text()
        year=self.ui.lineEdit_4.text()
        q_id=self.ui.lineEdit_5.text()
        e_mail=self.ui.lineEdit_6.text()
        msg=QMessageBox()
        msg.setWindowTitle("Thanks")
        msg.setText("Your Registration is successfull")
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()
    def back(self):
        self.wc=welcome()
        self.wc.show()
        self.hide()
class faculty(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_faculty()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.issue)
        self.ui.pushButton_5.clicked.connect(self.return1)
        self.ui.pushButton_3.clicked.connect(self.display)
        self.ui.pushButton_4.clicked.connect(self.add_book)
        self.ui.pushButton_6.clicked.connect(self.back)
    def back(self):
        self.wc=welcome()
        self.wc.show()
        self.hide()
    def display(self):
        print(listbook)
    def issue(self):
        self.iss=issue()
        self.iss.show()
        self.hide()
    def return1(self):
        self.rt=return1()
        self.rt.show()
        self.hide()
    def add_book(self):
        self.ad=add_book()
        self.ad.show()
        self.hide()
class issue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_issue()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.iss)
        self.ui.pushButton_2.clicked.connect(self.back)

    def iss(self):
        name=self.ui.lineEdit.text()
        book=self.ui.lineEdit_2.text()
        book_no=int(book)
        if(book_no not in listbook):
            print("we don't have this book")
        elif name in dict:
            print(f"{name}\t Book no :",dict[f"{name}"])
            print("We can't issue more books to you....")
        else:
            listbook.remove(book_no)
            dict[f"{name}"]=book_no
            print(f"{name}\t Book no :",dict[f"{name}"])
            print("now the remaining books are:",listbook)
    def back(self):
        self.wc=faculty()
        self.wc.show()
        self.hide()
class return1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_return1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.rt)
        self.ui.pushButton_2.clicked.connect(self.back)
    def rt(self):
        name=self.ui.lineEdit.text()
        book_no=int(self.ui.lineEdit_2.text())
        if name not in dict:
            print("Sorry No book issued to you")
        elif name in dict:
            print(f"{name}\t Book No. ",dict[f"{name}"])
            listbook.append(dict[f"{name}"])
            dict.pop(f"{name}")
    def back(self):
        self.wc=faculty()
        self.wc.show()
        self.hide()
class add_book(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_add_book()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ad)
        self.ui.pushButton_2.clicked.connect(self.back)
    def ad(self):
        c=int(self.ui.lineEdit_2.text())
        listbook.append(c)
        print("List of books that we have now: ",listbook) 
    def back(self):
        self.wc=faculty()
        self.wc.show()
        self.hide()
app=QApplication(sys.argv)
wc=welcome()
wc.show()
sys.exit(app.exec())
