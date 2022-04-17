from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import cryption as cry
from main import Ui_LastWindow
import mariadb
import sys

class Ui_MainWindow(object):

    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_LastWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def loginFunction(self):

        password=self.lineEdit_2.text()
        enPass=cry.encrypt_pass(password)
        try:
            connection = mariadb.connect(
                user = 'root',
                password = 'Kesandzsm3354',
                host = 'database-1.czrchfylrgcw.us-east-1.rds.amazonaws.com',
                port = 3306,
                database = 'pass1'
                )  
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)    

        """connection = sqlite3.connect('pass.db')
                                if (connection):
                                    print("Connection success")
                                else:
                                    print("Failed")"""

        veritabani_sec = connection.cursor()
        userspass = [(enPass[0] ,enPass[1] )]

        vt=connection.cursor()
        vt.execute("SELECT COUNT(password) FROM userpass ")
        data = vt.fetchall()

        if(data[0][0]==0):
            veritabani_sec.executemany("""INSERT INTO userpass (password,privateKey) VALUES (?,?)""", userspass)
            self.openWindow()
        elif(password==cry.decrypt_pass()):
            self.openWindow()

        else:
            self.warning("Alert","Please enter correct password")

        connection.commit()
        connection.close()

    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 482)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(185, 185, 185)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 220, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 14, 30)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginFunction)



        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 180, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 19, 34)")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PasswordSaver"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

        self.label_2.setText(_translate("MainWindow", "Password"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
