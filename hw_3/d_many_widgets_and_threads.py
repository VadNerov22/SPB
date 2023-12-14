"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets
from b_systeminfo_widget import Window
from c_weatherapi_widget import WindowWeather


class UWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        self.setWindowTitle("Объединенное окно")
        self.setFixedSize(350, 400)

        self.sisteminfo = Window()
        self.weatherapi = WindowWeather()

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.sisteminfo)
        main_layout.addWidget(self.weatherapi)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = UWindow()
    myWindow.show()

    app.exec()
