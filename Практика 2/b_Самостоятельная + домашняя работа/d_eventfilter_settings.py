"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения.
"""

from PySide6 import QtWidgets, QtGui, QtCore
from ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QtCore.QSettings("MyDataForm")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__initUi()
        self.__initSignals()
        self.loadData()

    def __initUi(self) -> None:
        """
        Доинициализация интерфейса

        :return: None
        """

        # dial -----------------------------------------------------------
        self.ui.dial.setRange(0, 100)  # размер ранжирования
        self.ui.dial.setSingleStep(1)  # шаг деления

        # Slider -----------------------------------------------------------
        self.ui.horizontalSlider.setRange(0, 100)  # размер ранжирования
        self.ui.horizontalSlider.setSingleStep(1)  # шаг деления

        # LcdNumber -----------------------------------------------------------
        i = len(bin(self.ui.dial.maximum()))
        self.ui.lcdNumber.setDigitCount(i)  # размер отображаемого числа

        # comboBox -----------------------------------------------------------
        self.ui.comboBox.addItem("Выберите систему счисления")
        self.ui.comboBox.addItem("Bin")
        self.ui.comboBox.addItem("Oct")
        self.ui.comboBox.addItem("Dec")
        self.ui.comboBox.addItem("Hex")

    def loadData(self) -> None:
        """
        Загрузка данных в Ui

        :return: None
        """

        self.ui.comboBox.setCurrentIndex(self.settings.value("comboBox", type=int))
        self.ui.lcdNumber.display(self.settings.value("lcdNumber", type=int))

    def __initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.dial.valueChanged.connect(lambda: self._ControlValueChange(self.ui.dial))
        self.ui.horizontalSlider.valueChanged.connect(lambda: self._ControlValueChange(self.ui.horizontalSlider))
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.show_box_item())

    # slots --------------------------------------------------------------
    def show_box_item(self) -> None:
        """
        Работа с comboBox.

        :return: None
        """

        if self.ui.comboBox.currentText() == "Выберите систему исчисления":
            self.ui.lcdNumber.value()

        elif self.ui.comboBox.currentText() == "Bin":
            self.ui.lcdNumber.setBinMode()

        elif self.ui.comboBox.currentText() == "Oct":
            self.ui.lcdNumber.setOctMode()

        elif self.ui.comboBox.currentText() == "Dec":
            self.ui.lcdNumber.setDecMode()

        elif self.ui.comboBox.currentText() == "Hex":
            self.ui.lcdNumber.setHexMode()

    def _ControlValueChange(self, w) -> None:
        """
        Синхранизация значения для dial и horizontalSlider.

        :param w: значение виджета
        :return: None
        """

        if w == self.ui.dial:
            self.ui.horizontalSlider.setValue(self.ui.dial.value())
            self.ui.lcdNumber.display(self.ui.dial.value())

        else:
            self.ui.dial.setValue(self.ui.horizontalSlider.value())
            self.ui.lcdNumber.display(self.ui.horizontalSlider.value())

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Событие нажатия на клавиатуру
        :param event: QtGui.QKeyEvent

        :return: None
        """

        if event.key() == 43:  # отработка клавиши "+"
            self.ui.dial.setValue(self.ui.dial.value() + 1)
            print(self.ui.dial.value())

        elif event.key() == 45:  # отработка клавиши "-"
            self.ui.dial.setValue(self.ui.dial.value() - 1)
            print(self.ui.dial.value())

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        self.settings.setValue("comboBox", self.ui.comboBox.currentIndex())
        self.settings.setValue("lcdNumber", self.ui.lcdNumber.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
