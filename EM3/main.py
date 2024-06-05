import math
import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextBrowser
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Оконное приложение с расчетами')
        self.setGeometry(100, 100, 800, 500)

        # Создаем виджеты для ввода данных
        self.mx_label = QLabel('Введите значение A:')
        self.mx_input = QLineEdit()
        self.mx_input.setFixedWidth(100)

        self.dx_label = QLabel('Введите значение B:')
        self.dx_input = QLineEdit()
        self.dx_input.setFixedWidth(100)

        self.n_label = QLabel('Введите значение N:')
        self.n_input = QLineEdit()
        self.n_input.setFixedWidth(100)

        # Создаем кнопку для запуска расчетов
        self.calculate_button = QPushButton('Рассчитать')

        # Создаем текстовые поля для вывода результатов
        self.x_values_text = QTextBrowser()
        self.delta_text = QTextBrowser()

        # Размещаем виджеты на главном макете
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.mx_label)
        input_layout.addWidget(self.mx_input)
        input_layout.addWidget(self.dx_label)
        input_layout.addWidget(self.dx_input)
        input_layout.addWidget(self.n_label)
        input_layout.addWidget(self.n_input)

        output_layout = QVBoxLayout()
        output_layout.addWidget(self.x_values_text)
        output_layout.addWidget(self.delta_text)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.calculate_button)
        button_layout.addStretch(1)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(output_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Привязываем метод calculate к событию нажатия на кнопку
        self.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        # ВВОД
        A = float(self.mx_input.text())
        B = float(self.dx_input.text())
        N = int(self.n_input.text())

        result_x_values = ""
        result_delta = ""

        arr_n_i = []
        for i in range(N):
            r_i = random.random()
            n_i = self.x_i_func(A, B, r_i)
            arr_n_i.append(n_i)

            if i < 20:
                result_x_values += f"X_{i + 1}: {n_i:.4f}   "

        Mx = (A + B) / 2
        Dx = (B - A) ** 2 / 12

        result_delta += f"\nΔ_1: {abs((Mx) - self.m(arr_n_i)):.4f}\n"
        result_delta += f"Δ_2: {abs((Dx) - self.d(arr_n_i)):.4f}\n\n"

        # Вывод результатов в текстовые поля
        self.x_values_text.setPlainText(result_x_values)
        self.delta_text.setPlainText(result_delta)

    # функция
    def f(self, x):
        if 0 < x < 1:
            return 0
        return x

    # x_i
    def x_i_func(self, A, B, r):
        return A + r * (B - A)

    # мат ожидание по формуле
    def m(self, arr):
        return sum(arr) / len(arr)

    # дисперсия по формуле
    def g(self, arr):
        summ = sum(map(lambda x: x ** 2, arr))
        return summ / len(arr) - self.m(arr) ** 2

    def d(self, arr):
        return len(arr) / (len(arr) - 1) * self.g(arr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
