from PySide6 import QtWidgets
from regestration_window import RegWindow
from ui.log import Ui_Form


def authenticate(login, password):
    db = {
        "ivan": "012345",
        "pavel": "987654321"
    }
    return db[login] == password


class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__intUi()
        self.__intSignal()

    def __intUi(self):
        self.ui.lineEdit_Pasword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def __intSignal(self):
        self.ui.pushButton_LoginOk.clicked.connect(self.__onPushButtonLoginOk)
        self.ui.pushButton_Regestration.clicked.connect(self.__onPushButtonRegestration)

    def __onPushButtonRegestration(self):
        self.__regestration_window = RegWindow()
        self.__regestration_window.registered.connect(self.__regestrationComplete)
        self.__regestration_window.exec()

    def __regestrationComplete(self, data):
        self.ui.lineEdit_Login.setText(data[0])
        self.ui.lineEdit_Pasword.setText(data[1])

    def __onPushButtonLoginOk(self):
        login = self.ui.lineEdit_Login.text()
        password = self.ui.lineEdit_Pasword.text()

        try:
            result = authenticate(login, password)
        except KeyError:
            print("Вы не зарегистрированы, пройдите регистрацию")
            return

        if result:
            print("Добро пожаловать,", login)
            return
        print("Введен неправильный пароль!")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MyFirstWindow()
    window.show()

    app.exec()
