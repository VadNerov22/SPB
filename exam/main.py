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
from PySide6 import QtWidgets, QtCore
from ui.auth import Ui_Form
from ui.tablew import Ui_MainWindow


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

        # Определяем стиль отображаемого окна
        with open('./ui/themes/MacOS.qss', 'r') as f:
            self.setStyleSheet(f.read())

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
            QtWidgets.QMessageBox.about(self, "Уведомление", "Соeдинение с базой данных установлено! \n \n ʕ•ᴥ•ʔ")

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

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUI()
        self.initSignals()

    def initUI(self) -> None:
        """
        Доинициализация интерфейса
        :return: None
        """

        self.setWindowTitle("Transport")
        self.createTable()

        # Добавляем действия на панель инструментов
        self.ui.menubar.addAction(self.ui.menu.menuAction())
        self.ui.menubar.addAction(self.ui.menu_2.menuAction())

        self.ui.menu.addAction(self.ui.addRowM)
        self.ui.menu.addAction(self.ui.editCellM)
        self.ui.menu.addAction(self.ui.delRowM)
        self.ui.menu_2.addAction(self.ui.abouteT)

        # Определяем стиль отображаемого окна
        with open('./ui/themes/MacOS.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """

        # Добавление строки
        self.ui.addRowM.triggered.connect(self.add_row)
        self.ui.pushButtonAddRow.clicked.connect(self.add_row)
        # Удаление строки
        self.ui.delRowM.triggered.connect(self.del_row)
        self.ui.pushButtonDelRow.clicked.connect(self.del_row)
        # Редактирование выбранной ячейки
        self.ui.editCellM.triggered.connect(lambda: self.ui.tableWidget.editItem(self.ui.tableWidget.currentItem()))
        # Выводим справку о таблице данных
        self.ui.abouteT.triggered.connect(self.show_message_about)
        # Сохранение данных в базу данных
        self.ui.pushButtonSave.clicked.connect(self.updateData)

    def createTable(self):
        """
        Функция создания объекта QTableWidget и закгрузки данных в таблицу из БД PostgreSQL
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
            cursor.execute('SELECT * FROM "Tcompany"."Transport";')

            # Получение результирующих строк
            rows = cursor.fetchall()
            self.ui.tableWidget.setRowCount(len(rows))
            self.ui.tableWidget.setColumnCount(8)

            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["transportid", "модель", "серийный_номер_ТС", "инд_рег_знак",
                 "год_выпуска", "срок_службы", "макс_пробег_до_списания",
                 "количество_посадочных_мест"]
            )

            # Установка данных в таблицу
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(i, j, item)

            self.ui.tableWidget.resizeColumnsToContents()

            # Закрытие курсора и соединения
            cursor.close()
            connection.close()

        except psycopg2.Error as Error:
            print(Error)

    def show_message_about(self) -> None:
        """
        Обработка сигнала кнопики меню abouteT
        :return: None
        """
        name = self.windowTitle()
        QtWidgets.QMessageBox.about(
                            self, f"О таблице '{name}' базы данных 'DevDB2023_vadyas'",
                            "Содержит информацию об автопарке транспортной компании: \n"
                            "'transportid' - id записи в БД (НЕ ЗАПОЛНЯТЬ!!!) \n"
                            "'модель' - модель транспортного средства, \n"
                            "'серийный_номер_ТС' - серийный номер транспортного средства, \n"
                            "'инд_рег_знак' - регистрационный знак транспортного средства,\n"
                            "'год_выпуска' - год выпуска транспортного средства (не старше 1950 г.), \n"
                            "'срок_службы' - срок эксплуатации транспортного средства, \n"
                            "'макс_пробег_до_списания' - остаток пробега до списания транспортного средства, \n"
                            "'количество_посадочных_мест' - количество пассажирских мест"
                                    )

    def add_row(self):
        """
        Добавление строки
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

            # Значения столбцов по умолчанию
            val = ['ОБРАЗЕЦ ДАННЫХ!', 'AB123456CD91234CD', 'К123РС086', 2023, 12.12, 1000000, 123]

            # SQL-запрос для добавления строки
            query = 'INSERT INTO "Tcompany"."Transport" (модель, "серийный_номер_ТС", ' \
                    'инд_рег_знак, год_выпуска, срок_службы, макс_пробег_до_списания, ' \
                    'количество_посадочных_мест) VALUES (%s, %s, %s, %s, %s, %s, %s);'

            cursor.execute(query, (val[0], val[1], val[2], val[3], val[4], val[5], val[6]))

            connection.commit()

            # Закрытие курсора и соединения
            cursor.close()
            connection.close()

        except psycopg2.Error as Error:
            QtWidgets.QMessageBox.warning(self, "Предупреждение", f"Данные введены не корректно: {Error}")

        # Очиста существующей таблицы
        self.ui.tableWidget.clear()
        # Обновление таблицы
        self.createTable()

    def del_row(self):
        """
        Удаление строки
        """

        # Получение индекса и значения первичного ключа выбранной строки
        primary_key_value = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()

        # Удаление строки из базы данных
        try:
            connection = psycopg2.connect(
                host="vpngw.avalon.ru",
                port="5432",
                database="DevDB2023_vadyas",
                user="pguser",
                password="Pa$$w0rd"
            )

            cursor = connection.cursor()
            # SQL-запрос для удаления строки
            cursor.execute('DELETE FROM "Tcompany"."Transport" WHERE transportid = %s;', (primary_key_value,))

            # Закрытие курсора и соединения
            connection.commit()
            cursor.close()
            connection.close()

        except psycopg2.Error as Error:
            print(Error)

        # Удаление строки из таблицы приложения
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    def updateData(self):
        """
        Функция обновления данных из таблицы в БД PostgreSQL
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

            for row in range(self.ui.tableWidget.rowCount()):
                values = []
                for column in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, column)
                    if item is not None:
                        value = item.text()
                    else:
                        value = ""
                    values.append(value)

                # Первый столбец - первичный ключ
                primary_key = values[0]
                # SQL-запрос для обновления и дополнительные параметры запроса
                query = 'UPDATE "Tcompany"."Transport" SET модель = %s, "серийный_номер_ТС" = %s,' \
                        ' инд_рег_знак = %s, год_выпуска = %s, срок_службы = %s, макс_пробег_до_списания = %s, ' \
                        'количество_посадочных_мест = %s WHERE transportid = %s'
                params = (values[1], values[2], values[3], values[4], values[5], values[6], values[7], primary_key)

                cursor.execute(query, params)

            # Закрытие курсора и соединения
            connection.commit()
            cursor.close()
            connection.close()

        except psycopg2.Error as Error:
            QtWidgets.QMessageBox.warning(self, "Предупреждение", f"Данные введены не корректно: {Error}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()

    win = DbAuthorization()
    win.show()

    sys.exit(app.exec())
