# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 250)
        Form.setMinimumSize(QSize(350, 250))
        Form.setMaximumSize(QSize(350, 250))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 304, 220))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelH = QLabel(self.widget)
        self.labelH.setObjectName(u"labelH")
        self.labelH.setMinimumSize(QSize(95, 0))
        self.labelH.setMaximumSize(QSize(95, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.labelH.setFont(font)

        self.horizontalLayout.addWidget(self.labelH)

        self.lineEditHost = QLineEdit(self.widget)
        self.lineEditHost.setObjectName(u"lineEditHost")

        self.horizontalLayout.addWidget(self.lineEditHost)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelP = QLabel(self.widget)
        self.labelP.setObjectName(u"labelP")
        self.labelP.setMinimumSize(QSize(95, 0))
        self.labelP.setMaximumSize(QSize(95, 16777215))
        self.labelP.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelP)

        self.lineEditPort = QLineEdit(self.widget)
        self.lineEditPort.setObjectName(u"lineEditPort")

        self.horizontalLayout_2.addWidget(self.lineEditPort)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelBD = QLabel(self.widget)
        self.labelBD.setObjectName(u"labelBD")
        self.labelBD.setMinimumSize(QSize(95, 0))
        self.labelBD.setMaximumSize(QSize(95, 16777215))
        self.labelBD.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelBD)

        self.lineEditBaseData = QLineEdit(self.widget)
        self.lineEditBaseData.setObjectName(u"lineEditBaseData")

        self.horizontalLayout_3.addWidget(self.lineEditBaseData)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_U = QLabel(self.widget)
        self.label_U.setObjectName(u"label_U")
        self.label_U.setMinimumSize(QSize(95, 0))
        self.label_U.setMaximumSize(QSize(95, 16777215))
        self.label_U.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_U)

        self.lineEditUser = QLineEdit(self.widget)
        self.lineEditUser.setObjectName(u"lineEditUser")

        self.horizontalLayout_4.addWidget(self.lineEditUser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_SP = QLabel(self.widget)
        self.label_SP.setObjectName(u"label_SP")
        self.label_SP.setMinimumSize(QSize(95, 0))
        self.label_SP.setMaximumSize(QSize(95, 16777215))
        self.label_SP.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_SP)

        self.lineEditPassword = QLineEdit(self.widget)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.lineEditPassword)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonSave = QPushButton(self.widget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setMinimumSize(QSize(0, 30))
        self.pushButtonSave.setMaximumSize(QSize(300, 30))

        self.verticalLayout.addWidget(self.pushButtonSave)

        self.pushButtonEnter = QPushButton(self.widget)
        self.pushButtonEnter.setObjectName(u"pushButtonEnter")
        self.pushButtonEnter.setMinimumSize(QSize(300, 30))
        self.pushButtonEnter.setMaximumSize(QSize(300, 30))

        self.verticalLayout.addWidget(self.pushButtonEnter)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0410\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0432 \u0411\u0414", None))
        self.labelH.setText(QCoreApplication.translate("Form", u"\u0425\u043e\u0441\u0442 :", None))
        self.labelP.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0440\u0442 :", None))
        self.labelBD.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 :", None))
        self.label_U.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c :", None))
        self.label_SP.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c :", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonEnter.setText(QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

