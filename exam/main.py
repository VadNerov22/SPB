"""
Задача.
Разработать клиент для работы с базой данных, разработка которой велась на курсе DevDB.
Обязательные функции в приложении:
* Должна присутствовать авторизация в БД
* Функционал должен обеспечивать полный набор CRUD операции с БД.
* Обеспечить возможность работы с клиентом (отображение данных в графических элементах).
- Данные для подключения к БД: host=vpngw.avalon.ru, port=5432, database=DevDB2023_vadyas,
user=pguser, password=Pa$$w0rd
"""
import sys

import psycopg2
from PySide6 import QtWidgets, QtCore, QtGui
from ui.auth import Ui_Form


class DbAuthorization(QtWidgets.QWidget):
    """
    Класс отвечающий за процедуру авторизации пользователя
    в базе данных
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QtCore.QSettings("MyBaseDataSQL")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.loadData()

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """

        self.ui.pushButtonEnter.clicked.connect(self.onPushButtonEnter)
        self.ui.pushButtonSave.clicked.connect(self.onPushButtonSave)

    def loadData(self) -> str:
        """
        Загрузка данных, ранее сохраненных пользователем
        :return: str
        """

        self.ui.lineEditBaseData.setText(self.settings.value("database"))
        self.ui.lineEditUser.setText(self.settings.value("user"))
        self.ui.lineEditPassword.setText(self.settings.value("password"))
        self.ui.lineEditHost.setText(self.settings.value("host"))
        self.ui.lineEditPort.setText(self.settings.value("port"))

    def onPushButtonEnter(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonEnter.
        Подключение к базе данных.

        :return: None
        """

        self.connection = psycopg2.connect(
            database=self.ui.lineEditBaseData.text(),
            user=self.ui.lineEditUser.text(),
            password=self.ui.lineEditPassword.text(),
            host=self.ui.lineEditHost.text(),
            port=self.ui.lineEditPort.text()
        )

        if self.connection:
            cursor = self.connection.cursor()
            QtWidgets.QMessageBox.about(self, "Уведомление", "Соeдинение с базой данных установлено!")

            cursor.execute('SELECT version()')
            print(cursor.fetchone())
            win.close()
            main_window.show()

    def onPushButtonSave(self) -> dict:
        """
        Обработка сигнала clicked для кнопки pushButtonSave.
        Сохраненние данных пользователя.

        :return: dict
        """

        self.settings.setValue("database", self.ui.lineEditBaseData.text())
        self.settings.setValue("user", self.ui.lineEditUser.text())
        self.settings.setValue("password", self.ui.lineEditPassword.text())
        self.settings.setValue("host", self.ui.lineEditHost.text())
        self.settings.setValue("port", self.ui.lineEditPort.text())


class MainWindow(QtWidgets.QMainWindow):
    """
     Класс отвечающий за работу с базой данных
     """

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self) -> None:
        """
        Инициализация интерфейса
        :return: None
            """

        self.setWindowTitle("База данных 'DevDB2023_vadyas'")
        self.setMinimumSize(800, 600)

        self.createTable()

        # Добавляем панель инструментов
        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)

        # Определяем функционал кнопок
        self.add_action = QtGui.QAction("Добавить")
        self.delete_action = QtGui.QAction("Удалить")
        self.edit_action = QtGui.QAction("Изменить")

        # Добавляем действия на панель инструментов
        toolbar.addAction(self.add_action)
        toolbar.addAction(self.delete_action)
        toolbar.addAction(self.edit_action)

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.add_action.triggered.connect(self.add_row)
        self.delete_action.triggered.connect(self.delete_row)
        self.edit_action.triggered.connect(self.edit_cell)

    def add_row(self):
        """
        Добавление строки
        """
        self.tableWidget.insertRow(self.tableWidget.rowCount())

    def delete_row(self):
        """
        Удаление строки
        """
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def edit_cell(self):
        """
        Редактирование выбранной ячейки
        """
        self.tableWidget.editItem(self.tableWidget.currentItem())

    def createTable(self):
        """
        Создание объекта QTableWidget
        """

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(8)

        self.tableWidget.setHorizontalHeaderLabels(["transportid", "модель", "серийный_номер_ТС", "инд_рег_знак",
                                                    "год_выпуска", "срок_службы", "макс_пробег_до_списания",
                                                    "количество_посадочных_мест"])

        self.loadData()

        self.tableWidget.resizeColumnsToContents()
        self.setCentralWidget(self.tableWidget)

    def loadData(self):
        """
        Функция закгрузки данных в таблицу из БД PostgreSQL
        """

        try:
            connection = psycopg2.connect(
                host="vpngw.avalon.ru",
                port="5432",
                database="DevDB2023_vadyas",
                user="pguser",
                password="Pa$$w0rd"
            )

            cursor = connection.cursor()

            # Выполнение запроса SELECT
            cursor.execute('SELECT * FROM "Tcompany"."Transport"')

            # Получение результирующих строк
            rows = cursor.fetchall()

            # Установка данных в таблицу
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)

            # Закрытие курсора и соединения
            cursor.close()
            connection.close()

        except psycopg2.Error as Error:
            print(Error)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()

    win = DbAuthorization()
    win.show()

    sys.exit(app.exec())
