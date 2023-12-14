"""
Модуль в котором содержаться потоки Qt
"""

import time
import requests
import psutil
from PySide6 import QtCore, QtWidgets


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.delay = None

    def run(self) -> None:
        if self.delay is None:  # Если задержка не передана в поток перед его запуском
            self.delay = 1  # Tо устанавливайте значение 1

        while True:
            # Запуск бесконечного цикла получения информации о системе
            cpu_value = psutil.cpu_percent()  # Получаем загрузку CPU
            ram_value = psutil.virtual_memory().percent  # Получаем загрузку RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])  # Передаем в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # Приостановливаем выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    weatherHandlerReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        if self.__delay is None and self.__api_url is None:
            return

        self.__status = True

        while self.__status:
            try:
                response = requests.get(self.__api_url)
                data = response.json()
                self.weatherHandlerReceived.emit(data)
                time.sleep(self.__delay)
            except requests.exceptions.MissingSchema:
                self.weatherHandlerReceived.emit(-1)
                time.sleep(self.__delay)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    # t = SystemInfo()
    # t.systemInfoReceived.connect(lambda data: print(data))
    # t.start()
    #
    # w = WeatherHandler(44.96, 34.11)
    # w.weatherHandlerReceived.connect(lambda data: print(data))
    # w.start()

    app.exec()
