from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        # label ----------------------------------------------------------
        labelLogin = QtWidgets.QLabel("Логин")
        labelLogin.setMinimumWidth(70)  # установил минимальную ширину для более лучшего отображения
        labelRegistration = QtWidgets.QLabel("Регистрация")
        labelRegistration.setMinimumWidth(70)  # установил минимальную ширину для более лучшего отображения

        # lineEdit -----------------------------------------------------------
        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Введите логин")
        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setPlaceholderText("Введите пароль")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # pushButton -----------------------------------------------------------
        self.pushButtonLogin = QtWidgets.QPushButton()
        self.pushButtonLogin.setText("Войти")

        self.pushButtonRegistration = QtWidgets.QPushButton()
        self.pushButtonRegistration.setText("Регистрация")

        # Login layout -----------------------------------------------------------
        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        # Password layout -----------------------------------------------------------
        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(labelRegistration)
        layoutPassword.addWidget(self.lineEditPassword)

        # Buttons layout -----------------------------------------------------------
        layoutButtons = QtWidgets.QHBoxLayout()
        layoutButtons.addWidget(self.pushButtonLogin)
        layoutButtons.addWidget(self.pushButtonRegistration)

        # main layout
        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addLayout(layoutButtons)

        self.setLayout(layoutMain)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
