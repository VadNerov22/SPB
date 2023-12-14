"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""

import time
from PySide6 import QtWidgets
from a_threads import WeatherHandler


class WindowWeather(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.lat = 44.96
        self.lon = 34.11
        self.request_thread = WeatherHandler(self.lat, self.lon)

        self.initUI()
        self.initSignals()

    def initUI(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        self.setWindowTitle("Погода")
        self.setFixedSize(320, 280)

        labelDelay = QtWidgets.QLabel("Интервал обновления, с")
        self.spinBoxDelay = QtWidgets.QSpinBox()
        # self.spinBoxDelay.setMinimum(1)

        lDelay = QtWidgets.QHBoxLayout()
        lDelay.addWidget(labelDelay)
        lDelay.addWidget(self.spinBoxDelay)

        labelLat = QtWidgets.QLabel("Широта")
        labelLat.setMinimumWidth(50)
        self.lineEditLat = QtWidgets.QLineEdit()

        lLat = QtWidgets.QHBoxLayout()
        lLat.addWidget(labelLat)
        lLat.addWidget(self.lineEditLat)

        labelLong = QtWidgets.QLabel("Долгота")
        labelLong.setMinimumWidth(50)
        self.lineEditLong = QtWidgets.QLineEdit()

        lLong = QtWidgets.QHBoxLayout()
        lLong.addWidget(labelLong)
        lLong.addWidget(self.lineEditLong)

        labelWeather = QtWidgets.QLabel("Погода")
        labelWeather.setMinimumWidth(50)
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        lPl = QtWidgets.QVBoxLayout()
        lPl.addWidget(labelWeather)
        lPl.addWidget(self.plainTextEdit)

        self.pbHandle = QtWidgets.QPushButton("Старт")
        self.pbHandle.setCheckable(True)

        lPbh = QtWidgets.QVBoxLayout()
        lPbh.addWidget(labelWeather)
        lPbh.addWidget(self.pbHandle)

        lMain = QtWidgets.QVBoxLayout()
        lMain.addLayout(lLat)
        lMain.addLayout(lLong)
        lMain.addLayout(lDelay)
        lMain.addLayout(lPl)
        lMain.addLayout(lPbh)

        self.setLayout(lMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.lineEditLat.textChanged.connect(self.change_lat)
        self.lineEditLong.textChanged.connect(self.change_long)

        self.spinBoxDelay.valueChanged.connect(self.request_thread.setDelay)
        self.pbHandle.clicked.connect(self.onPbHandleClicked)
        self.request_thread.weatherHandlerReceived.connect(self.getWeather)

    def change_lat(self, text) -> float:
        """
         Изменение и валидация координат широты

        :param text: введенные (изменныне) координаты широты
        :return: float
        """

        if -90 <= float(text) <= 90:
            self.lat = float(text)
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите корректные координаты!")
            self.lineEditLat.clear()

    def change_long(self, text) -> float:
        """
         Изменение и валидация координат долготы

        :param text: введенные (изменныне) координаты долготы
        :return: float
        """

        if -180 <= float(text) <= 180:
            self.lon = float(text)
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите корректные координаты!")
            self.lineEditLong.clear()

    def onPbHandleClicked(self, status) -> None:
        """
        Обработка сигнала clicked для кнопки PbHandleClicked

        :return: None
        """

        if status and not self.request_thread.start():
            self.request_thread.start()
            self.spinBoxDelay.setEnabled(False)
            self.lineEditLat.setEnabled(False)
            self.lineEditLong.setEnabled(False)
        else:
            self.request_thread.terminate()
            self.spinBoxDelay.setEnabled(True)
            self.lineEditLat.setEnabled(True)
            self.lineEditLong.setEnabled(True)

        self.pbHandle.setText("Стоп" if status else "Старт")

    def getWeather(self, wdata: dict) -> None:
        """
        Вывод информации о погоде с потока

        :return: None
        """

        latitude = wdata['latitude']
        longitude = wdata['longitude']
        currentTime = wdata['current_weather']['time']
        temperature = wdata['current_weather']['temperature']
        winddirection = wdata['current_weather']['winddirection']
        windspeed = wdata['current_weather']['windspeed']

        self.plainTextEdit.setPlainText(
            f"Широта: {latitude}° и Долгота: {longitude}° метеостанции\n"
            f"Дата: {currentTime} \n"
            f"Температура: {temperature}°C \n"
            f"Направление ветра: {winddirection}°\n"
            f"Скорость ветра: {windspeed} м/c"
        )

        #print(f"{time.ctime()} >>> {self.lat, self.lon}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()
