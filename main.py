import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.load_data()

    def load_data(self):
        cursor = self.connection.cursor()
        query = "SELECT id, name, roast_degree, ground_or_beans, description, price, package_volume FROM coffee"
        result = cursor.execute(query).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название сорта", "Степень обжарки", "Тип", "Описание вкуса", "Цена", "Объем"]
        )
        for row_index, row_data in enumerate(result):
            for column_index, data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
