from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5 import QtWidgets, QtSql
from PyQt5.QtCore import  Qt
from app import *
import sys
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setEnabled(True)
        self.label_header.setStyleSheet("font: 25pt \"Segoe UI Black\";padding: 15px;")
        self.label_header.setObjectName("label_header")
        self.label_header.setAlignment(Qt.AlignCenter)
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setStyleSheet("font: 14pt \"Sitka Small\";")
        self.b1.setFixedSize(160, 40)
        self.b1.setObjectName("pushButton")
        self.b1.setText("Далее")
        self.b1.clicked.connect(self.button_clicked)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setStyleSheet("font: 14pt \"Sitka Small\";")
        self.b2.setFixedSize(160, 40)
        self.b2.setObjectName("pushButton2")
        self.b2.setText("Назад")
        self.b2.clicked.connect(self.button_clicked2)
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setStyleSheet("font:  16pt \"Segoe UI Semibold\";")
        self.label_input.setObjectName("label_input")
        self.label_input.setWordWrap(True)
        self.label_input.setAlignment(Qt.AlignCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.b1)
        self.horizontalLayout.addWidget(self.b2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.label_header)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.label_input)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist.db')
        if not self.db.open():
            print("Unable to connect to the database")
            sys.exit(1)
        self.db = QSqlQuery()
        self.db.exec("SELECT Событие FROM field")
        self.db.seek(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def button_clicked(self):
        self.db.next()
        print(self.db.value(0))
        self.label_input.setText(self.db.value(0))
    def button_clicked2(self):
        self.db.previous()
        print(self.db.value(0))
        self.label_input.setText(self.db.value(0))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_header.setText(_translate("MainWindow", "История Калининградской области"))
        self.label_input.setText(_translate("MainWindow", "Нажмите кнопку \"Далее\", чтобы изучить историю Калининградской области"))
        self.horizontalLayout.addWidget(self.b1)