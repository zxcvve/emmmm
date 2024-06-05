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
        self.setGeometry(100, 100, 750  , 500)

        # Создаем виджеты для ввода данных
        self.lambda_label = QLabel('Введите значение λ:')
        self.lambda_input = QLineEdit()
        self.lambda_input.setFixedWidth(100)

        self.n_label = QLabel('Введите значение N:')
        self.n_input = QLineEdit()
        self.n_input.setFixedWidth(100)

        self.d1_label = QLabel("Δ1 = ")
        self.d1_input = QLineEdit()
        self.d1_input.setReadOnly(True)
        self.d1_input.setFixedWidth(100)

        self.d2_label = QLabel("Δ2 = ")
        self.d2_input = QLineEdit()
        self.d2_input.setReadOnly(True)
        self.d2_input.setFixedWidth(100)


        # Создаем кнопку для запуска расчетов
        self.calculate_button = QPushButton('Рассчитать')

        # Создаем текстовые поля для вывода результатов
        self.x_values_text = QTextBrowser()
        self.delta_text = QTextBrowser()
        self.mean = QTextBrowser()

        # Размещаем виджеты на главном макете
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.lambda_label)
        input_layout.addWidget(self.lambda_input)
        input_layout.addWidget(self.n_label)
        input_layout.addWidget(self.n_input)
        # input_layout.addWidget(self.mean)

        output_layout = QVBoxLayout()
        output_layout.addWidget(self.x_values_text)
        # output_layout.addWidget(self.delta_text)
        output_layout.addWidget(self.d1_label)
        output_layout.addWidget(self.d1_input)
        # output_layout.addStretch(1)
        output_layout.addWidget(self.d2_label)
        output_layout.addWidget(self.d2_input)
        # output_layout.addStretch(1)


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
        try:
            # ВВОД
            lambda_val = float(self.lambda_input.text())
            N = int(self.n_input.text())
        except ValueError:
            self.x_values_text.setPlainText("Пожалуйста, введите корректные числовые значения.")
            return

        result_x_values = ""
        result_delta = ""

        arr_n_i = []
        for i in range(N):
            r_i = random.random()
            n_i = self.x_i_func(lambda_val, r_i)
            arr_n_i.append(n_i)

            if i < 20:
                result_x_values += f"{n_i:.4f}   "

        Mx = 1 / lambda_val
        Dx = 1 / (lambda_val ** 2)

        result_delta += f"Δ_1: {abs((Mx) - self.m(arr_n_i)):.4f}\n"
        result_delta += f"Δ_2: {abs((Dx) - self.d(arr_n_i)):.4f}\n\n"
        result_delta1= round(abs((Mx) - self.m(arr_n_i)),4)
        result_delta2= round(abs((Dx) - self.m(arr_n_i)),4)
        self.d1_input.setText(str(result_delta1))
        self.d2_input.setText(str(result_delta2))

        mean_string = f"Mx = {str(round(Mx,4))}\r"
        mean_string += f"m = {str(round(self.m(arr_n_i),4))}"
        self.mean.setPlainText(mean_string)
        



        # Вывод результатов в текстовые поля
        self.x_values_text.setPlainText(result_x_values)
        self.delta_text.setPlainText(result_delta)

    # функция
    def f(self, x):
        return self.lambda_val * math.exp(-self.lambda_val * x)

    # x_i
    def x_i_func(self, lambda_val, r):
        return -1/lambda_val*math.log(1-r)

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

# 
# отделные окна дл делта 1 и 2