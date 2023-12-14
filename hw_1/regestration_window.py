from PySide6 import QtWidgets, QtCore
from ui.regestration import Ui_Dialog


class RegWindow(QtWidgets.QDialog):
    registered = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.__intSignal()

    def __intSignal(self):
        self.ui.pushButton_Ok.clicked.connect(self.__onPushButtonOk)
        self.setWindowTitle("Регистрация")

    def __onPushButtonOk(self):
        login = self.ui.lineEdit_Login.text()

        if self.ui.lineEdit_Password.text() != self.ui.lineEdit_PasswordReap.text():
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введенные пароли не совпадают!")
            return

        password = self.ui.lineEdit_Password.text()

        #if regestration_success(login, password):
        self.registered.emit((login, password))
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = RegWindow()
    window.show()

    #window.registered.connect(lambda data: print(data))  #для проверки любого окна

    app.exec()
