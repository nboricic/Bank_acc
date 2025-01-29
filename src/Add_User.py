
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from DatabaseMng import creator

class Ui_add_a_new_user(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi()
    
    def back_to_main_manu(self, window1):
        self.window1 = window1
    def back_to_main(self):
        self.close()
        self.window1.show()
    
    def setupUi(self):
        self.setObjectName("add_a_new_user")
        self.resize(317, 381)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        

        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(120, 20, 171, 20))
        self.firstName.setObjectName("firstName")
        self.middleName = QtWidgets.QLineEdit(self.centralwidget)
        self.middleName.setGeometry(QtCore.QRect(120, 50, 171, 20))
        self.middleName.setObjectName("middleName")

        self.familyName = QtWidgets.QLineEdit(self.centralwidget)
        self.familyName.setGeometry(QtCore.QRect(120, 80, 171, 20))
        self.familyName.setObjectName("familyName")
        
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(120, 110, 171, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.dateChanged.connect(self.dateEdit.date)


        self.placeBirth = QtWidgets.QLineEdit(self.centralwidget)
        self.placeBirth.setGeometry(QtCore.QRect(120, 140, 171, 20))
        self.placeBirth.setObjectName("placeBirth")
        self.StateBirth = QtWidgets.QLineEdit(self.centralwidget)
        self.StateBirth.setGeometry(QtCore.QRect(120, 170, 171, 20))
        self.StateBirth.setObjectName("StateBirth")
        self.JMBG = QtWidgets.QLineEdit(self.centralwidget)
        self.JMBG.setGeometry(QtCore.QRect(20, 230, 271, 20))
        self.JMBG.setObjectName("JMBG")
        self.adressofLiving = QtWidgets.QLineEdit(self.centralwidget)
        self.adressofLiving.setGeometry(QtCore.QRect(20, 270, 271, 20))
        self.adressofLiving.setObjectName("adressofLiving")
       
        self.addUser = QtWidgets.QPushButton(self.centralwidget)
        self.addUser.setGeometry(QtCore.QRect(20, 310, 91, 23))
        self.addUser.setObjectName("addUser")
        self.addUser.clicked.connect(self.add_b_user)


        self.clearUSer = QtWidgets.QPushButton(self.centralwidget)
        self.clearUSer.setGeometry(QtCore.QRect(120, 310, 81, 23))
        self.clearUSer.setObjectName("clearUSer")
        self.clearUSer.clicked.connect(self.cleanContent)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(210, 310, 81, 23))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.back_to_main)
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.StatusBar = QtWidgets.QStatusBar(self)
        self.StatusBar.setObjectName("StatusBar")
        self.setStatusBar(self.StatusBar)
        self.actionClear = QtWidgets.QAction(self)
        self.actionClear.setObjectName("actionClear")
        self.actionClose = QtWidgets.QAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout_Software = QtWidgets.QAction(self)
        self.actionAbout_Software.setObjectName("actionAbout_Software")
        self.actionHelp = QtWidgets.QAction(self)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout_Software)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("add_a_new_user", "MainWindow"))
        self.label.setText(_translate("add_a_new_user", "First Name"))
        self.label_2.setText(_translate("add_a_new_user", "Middle name"))
        self.label_3.setText(_translate("add_a_new_user", "Family name"))
        self.label_4.setText(_translate("add_a_new_user", "Date of birth"))
        self.label_5.setText(_translate("add_a_new_user", "Place of birth"))
        self.label_6.setText(_translate("add_a_new_user", "State of birth"))
        self.label_7.setText(_translate("add_a_new_user", "Personal idetification number"))
        self.label_8.setText(_translate("add_a_new_user", "Adreess of living"))
        self.addUser.setText(_translate("add_a_new_user", "Add User"))
        self.clearUSer.setText(_translate("add_a_new_user", "Clear"))
        self.closeButton.setText(_translate("add_a_new_user", "Close"))
        self.menuFile.setTitle(_translate("add_a_new_user", "File"))
        self.menuHelp.setTitle(_translate("add_a_new_user", "Help"))
        self.actionClear.setText(_translate("add_a_new_user", "Clear"))
        self.actionClose.setText(_translate("add_a_new_user", "Close"))
        self.actionAbout_Software.setText(_translate("add_a_new_user", "About Software"))
        self.actionHelp.setText(_translate("add_a_new_user", "Help"))

    def add_b_user(self):
        print(type(self.familyName.text()))
        if self.firstName.text() == "":
           mesb = "first name"
           chck = 0
           self.popupMessage(mesb,chck)
        if self.middleName.text() == "":
           mesb = "middle name"
           chck = 0
           self.popupMessage(mesb,chck)
        if self.familyName.text() == "":
           mesb = "Family name"
           chck = 0
           self.popupMessage(mesb,chck)
        if self.placeBirth.text() == "":
           mesb = "place of birth"
           chck = 0
           self.popupMessage(mesb,chck)
        if self.StateBirth.text() == "":
           mesb = "State of birth"
           chck = 0
           self.popupMessage(mesb,chck)
        if self.JMBG.text() == "":
           mesb = "Personal idetification number"
           chck = 0
           self.popupMessage(mesb,chck)
        if self.adressofLiving.text() == "":
           chck = 0
           mesb = "Adress of living"
           self.popupMessage(mesb,chck)  
        
        else:
           mesb = "Data is succesfuly entered"
           chck = 1
           
           creator.create_bank_user(self.firstName.text(),self.middleName.text(),self.familyName.text(), self.dateEdit.date().toString("yyyy-MM-dd"), self.placeBirth.text(),
                             self.StateBirth.text(), self.JMBG.text(), self.adressofLiving.text())
           self.popupMessage(mesb,chck)  
           self.cleanContent()

    def popupMessage(self,mesb,chck):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Message")
        if chck == 0: 
           msg.setText(f"Field {mesb} is not entered")
        else:
           msg.setText(f"{mesb}")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.addButton(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    def cleanContent(self):
        self.firstName.clear()
        self.middleName.clear()
        self.familyName.clear()
        self.placeBirth.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.adressofLiving.clear()
        self.JMBG.clear()
        self.StateBirth.clear()
