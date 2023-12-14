"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtGui, QtCore
from ui.c_signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__initSignals()

    def __initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.pushButtonCenter.clicked.connect(self._moveCenterPosWindow)
        self.ui.pushButtonLT.clicked.connect(self._moveLTPosWindow)
        self.ui.pushButtonLB.clicked.connect(self._moveLBPosWindow)
        self.ui.pushButtonRT.clicked.connect(self._moveRTPosWindow)
        self.ui.pushButtonRB.clicked.connect(self._moveRBPosWindow)
        self.ui.pushButtonMoveCoords.clicked.connect(self._moveCoordsPosWindow)
        self.ui.pushButtonGetData.clicked.connect(self._GetData)

    # slots --------------------------------------------------------------
    def _moveLTPosWindow(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLT.
        Перемещение окна в левый верхний угол "доступного" экрана.

        :return: None
        """

        lt = QtGui.QScreen.availableGeometry(
            QtWidgets.QApplication.primaryScreen()).topLeft()  # определяем левый верхний угол "доступного" экрана
        self.move(lt)

    def _moveRTPosWindow(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRT.
        Перемещение окна в правый верхний угол "доступного" экрана.

        :return: None
        """

        rt = QtGui.QScreen.availableGeometry(
            QtWidgets.QApplication.primaryScreen()).topRight()  # определяем правый верхний угол "доступного" экрана
        # перемещаем окно приложения в правый верхний угол экрана
        Wframe = self.frameGeometry()
        Wframe.moveTopRight(rt)
        self.move(Wframe.topLeft())

    def _moveLBPosWindow(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLB.
        Перемещение окна в левый нижний угол "доступного" экрана.

        :return: None
        """

        lb = QtGui.QScreen.availableGeometry(
            QtWidgets.QApplication.primaryScreen()).bottomLeft()  # определяем левый нижний угол "доступного" экрана
        # перемещаем окно приложения в левый нижний угол экрана
        Wframe = self.frameGeometry()
        Wframe.moveBottomLeft(lb)
        self.move(Wframe.topLeft())

    def _moveRBPosWindow(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRB.
        Перемещение окна в правый нижний угол "доступного" экрана.

        :return: None
        """

        rb = QtGui.QScreen.availableGeometry(
            QtWidgets.QApplication.primaryScreen()).bottomRight()  # определяем правый нижний угол "доступного" экрана
        # перемещаем окно приложения в правый нижний угол экрана
        Wframe = self.frameGeometry()
        Wframe.moveBottomRight(rb)
        self.move(Wframe.topLeft())

    def _moveCenterPosWindow(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonCenter.
        Перемещение окна в центр "доступного" экрана.

        :return: None
        """

        Sсenter = QtGui.QScreen.availableGeometry(
            QtWidgets.QApplication.primaryScreen()).center()  # определяем центр "доступного" экрана
        # перемещаем окно приложения в центр экрана
        Wframe = self.frameGeometry()
        Wframe.moveCenter(Sсenter)
        self.move(Wframe.topLeft())

    def _moveCoordsPosWindow(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonMoveCoords.
        Перемещение окна по заданным координатам.

        :return: None
        """

        x = self.ui.spinBoxX.value()
        y = self.ui.spinBoxY.value()
        self.move(x, y)

    def _GetData(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonGetData.
        Получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
        * Кол-во экранов
        * Текущее основное окно
        * Разрешение экрана
        * На каком экране окно находится
        * Размеры окна
        * Минимальные размеры окна
        * Текущее положение (координаты) окна
        * Координаты центра приложения
        * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)

        :return: None
        """

        # определяем количество экранов
        sc = QtCore.QCoreApplication.instance()
        scre = len(sc.screens())
        self.ui.plainTextEdit.setPlainText(
            f"Дата: <<{time.ctime()}>> Количество экранов = {scre} \n"
            f"Дата: <<{time.ctime()}>> Текущее основное окно - '{QtGui.QGuiApplication.focusWindow().title()}' \n"
            f"Дата: <<{time.ctime()}>> Разрешение экрана: "
            f"{QtGui.QScreen.size(QtWidgets.QApplication.primaryScreen()).toTuple()} \n"
            f"Дата: <<{time.ctime()}>> Окно находится на экране монитора - "
            f"'{QtGui.QGuiApplication.screens()[0].name()}'\n"
            f"Дата: <<{time.ctime()}>> Размер окна: {QtGui.QGuiApplication.focusWindow().size().toTuple()} \n"
            f"Дата: <<{time.ctime()}>> Минимальный размер окна: "
            f"{QtGui.QGuiApplication.focusWindow().minimumSize().toTuple()} \n"
            f"Дата: <<{time.ctime()}>> Текущее положение (координаты) окна: "
            f"{QtGui.QGuiApplication.focusWindow().framePosition().toTuple()} \n"
            f"Дата: <<{time.ctime()}>> Координаты центра приложения: "
            f"{QtGui.QGuiApplication.focusWindow().frameGeometry().center().toTuple()} \n"
        )

    def event(self, event: QtCore.QEvent) -> bool:
        """
        Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено).
        При перемещении окна выводить его старую и новую позицию.
        При изменении размера окна выводить его новый размер.

        :param event:  QtCore.QEvent
        :return: bool
        """

        # Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено).
        if type(event) == QtGui.QWindowStateChangeEvent:
            if self.isMinimized():
                self.ui.plainTextEdit.setPlainText(f"Дата: <<{time.ctime()}>> Состояние окна: <<Окно свернуто>>")
            elif self.isMaximized():
                self.ui.plainTextEdit.setPlainText(f"Дата: <<{time.ctime()}>> Состояние окна: <<Окно развёрнуто>>")
            elif self.isActiveWindow():
                self.ui.plainTextEdit.setPlainText(f"Дата: <<{time.ctime()}>> Состояние окна: <<Окно активно>>")
            elif self.isVisible():
                self.ui.plainTextEdit.setPlainText(f"Дата: <<{time.ctime()}>> Состояние окна: <<Окно отображено>>")

        # При перемещении окна выводить его старую и новую позицию
        elif type(event) == QtGui.QMoveEvent:
            if self.moveEvent:
                print(f"Дата: <<{time.ctime()}>> старая позиция {event.oldPos().toTuple()}, "
                      f"новая позиция {event.pos().toTuple()}")

        # При изменении размера окна выводить его новый размер
        elif type(event) == QtGui.QResizeEvent:
            if self.resizeEvent:
                print(f"Дата: <<{time.ctime()}>> старый размер окна {event.oldSize().toTuple()}, "
                      f"новый размер окна {event.size().toTuple()}")

        return super(Window, self).event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
