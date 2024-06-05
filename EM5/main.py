import random
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, \
    QMessageBox
import sys
import math


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Окно')
        self.setGeometry(450, 450, 900, 500)

        self.setStyleSheet("background-color:#faf8f0;")

        self.a_label = QLabel('Введите значение A:')
        self.a_input = QLineEdit()
        self.a_input.setFixedWidth(100)
        self.a_input.setFixedHeight(40)
        self.a_input.setStyleSheet("background-color:white;")
        font = self.a_input.font()
        font.setPointSize(16)
        self.a_input.setFont(font)

        self.b_label = QLabel('Введите значение Сигмы:')
        self.b_input = QLineEdit()
        self.b_input.setFixedWidth(100)
        self.b_input.setFixedHeight(40)
        self.b_input.setStyleSheet("background-color:white;")
        font = self.b_input.font()
        font.setPointSize(16)
        self.b_input.setFont(font)

        self.n_label = QLabel('Введите значение N:')
        self.n_input = QLineEdit()
        self.n_input.setFixedWidth(100)
        self.n_input.setFixedHeight(40)
        self.n_input.setStyleSheet("background-color:white;")
        font = self.n_input.font()
        font.setPointSize(16)
        self.n_input.setFont(font)

        self.calculate_button = QPushButton('Рассчитать')
        self.calculate_button.setStyleSheet("padding: 15px; background-color: white")
        font = self.calculate_button.font()
        font.setPointSize(13)
        self.calculate_button.setFont(font)

        self.result_text = QTextEdit()
        self.result_text.setStyleSheet("background-color: white")
        self.result_text.setFontPointSize(14)
        self.result_text.setFixedHeight(200)

        self.delta_text = QTextEdit()
        self.delta_text.setStyleSheet("background-color: white")
        self.delta_text.setFontPointSize(14)
        self.delta_text.setReadOnly(True)
        self.delta_text.setFixedHeight(100)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.a_label)
        hbox1.addWidget(self.a_input)
        hbox1.addWidget(self.b_label)
        hbox1.addWidget(self.b_input)
        hbox1.addWidget(self.n_label)
        hbox1.addWidget(self.n_input)

        layout = QVBoxLayout()
        layout.addLayout(hbox1)
        layout.addWidget(self.result_text)
        layout.addWidget(self.delta_text)
        layout.addWidget(self.calculate_button)
        layout.addStretch(1)
        self.setLayout(layout)

        self.calculate_button.clicked.connect(self.calculate)

    def m(self, arr):
        return round((sum(arr)) / len(arr), 4)

    def d(self, arr):
        summ = 0
        n = len(arr)
        for i in range(n):
            summ += arr[i] ** 2
        return round((summ / (n - 1)) - (n / (n - 1)) * (self.m(arr) ** 2), 4)

    def calculate(self):
        A = float(self.a_input.text())
        S = float(self.b_input.text())
        N = int(self.n_input.text())

        S = S ** 2

        arr = []
        result_str = ''
        for j in range(min(N, 20)):
            summ = 0
            for i in range(12):
                r = random.random()
                summ += r

            x_i = summ - 6
            z_i = S * x_i + A
            arr.append(z_i)
            result_str += "{0:.4f}".format(z_i) + '  '

        self.result_text.clear()
        self.result_text.append(result_str)

        delta_1 = abs(A - self.m(arr))
        delta_2 = abs(S - self.d(arr))

        self.delta_text.clear()
        self.delta_text.append(f'Δ_1: {delta_1:.4f}\nΔ_2: {delta_2:.4f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
