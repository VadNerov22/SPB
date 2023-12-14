# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(260, 180)
        Form.setMinimumSize(QSize(230, 180))
        Form.setMaximumSize(QSize(260, 180))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_Login = QLineEdit(Form)
        self.lineEdit_Login.setObjectName(u"lineEdit_Login")

        self.horizontalLayout.addWidget(self.lineEdit_Login)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_Pasword = QLineEdit(Form)
        self.lineEdit_Pasword.setObjectName(u"lineEdit_Pasword")

        self.horizontalLayout_2.addWidget(self.lineEdit_Pasword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkBox_AutoEneter = QCheckBox(Form)
        self.checkBox_AutoEneter.setObjectName(u"checkBox_AutoEneter")

        self.verticalLayout.addWidget(self.checkBox_AutoEneter)

        self.pushButton_LoginOk = QPushButton(Form)
        self.pushButton_LoginOk.setObjectName(u"pushButton_LoginOk")

        self.verticalLayout.addWidget(self.pushButton_LoginOk)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_FogPasword = QPushButton(Form)
        self.pushButton_FogPasword.setObjectName(u"pushButton_FogPasword")

        self.horizontalLayout_3.addWidget(self.pushButton_FogPasword)

        self.pushButton_Regestration = QPushButton(Form)
        self.pushButton_Regestration.setObjectName(u"pushButton_Regestration")

        self.horizontalLayout_3.addWidget(self.pushButton_Regestration)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_Login.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_Pasword.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.checkBox_AutoEneter.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0432\u0445\u043e\u0434", None))
        self.pushButton_LoginOk.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.pushButton_FogPasword.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.pushButton_Regestration.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

