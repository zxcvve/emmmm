import random
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
)
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculation Tool")
        self.setStyleSheet("background-color:#faf8f0;")

        self.a_label = QLabel("Введите значение A:")
        self.a_input = QLineEdit()
        self.setup_input(self.a_input)

        self.b_label = QLabel("Введите значение Сигмы:")
        self.b_input = QLineEdit()
        self.setup_input(self.b_input)

        self.n_label = QLabel("Введите значение N:")
        self.n_input = QLineEdit()
        self.setup_input(self.n_input)

        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px; 
                background-color: #6c757d; 
                color: white; 
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)

        self.result_text = QTextEdit()
        self.result_text.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 1px solid #ced4da;
                border-radius: 10px;
                font-size: 16px;
                padding: 10px;
            }
        """)
        self.result_text.setReadOnly(True)

        self.delta_text1_label = QLabel("Δ_1:")
        self.delta_text1 = QLineEdit()
        self.setup_output(self.delta_text1)

        self.delta_text2_label = QLabel("Δ_2:")
        self.delta_text2 = QLineEdit()
        self.setup_output(self.delta_text2)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.a_label)
        hbox1.addWidget(self.a_input)
        hbox1.addWidget(self.b_label)
        hbox1.addWidget(self.b_input)
        hbox1.addWidget(self.n_label)
        hbox1.addWidget(self.n_input)
        hbox1.addStretch()

        delta_layout = QHBoxLayout()
        delta_layout.addWidget(self.delta_text1_label)
        delta_layout.addWidget(self.delta_text1)
        delta_layout.addWidget(self.delta_text2_label)
        delta_layout.addWidget(self.delta_text2)
        delta_layout.addStretch()

        layout = QVBoxLayout()
        layout.addLayout(hbox1)
        layout.addLayout(delta_layout)
        layout.addWidget(self.result_text)
        layout.addWidget(self.calculate_button)
        layout.addStretch()
        self.setLayout(layout)

        self.calculate_button.clicked.connect(self.calculate)

    def setup_input(self, input_widget):
        input_widget.setFixedWidth(100)
        input_widget.setFixedHeight(40)
        input_widget.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #ced4da;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
            }
        """)

    def setup_output(self, output_widget):
        output_widget.setFixedWidth(140)
        output_widget.setFixedHeight(40)
        output_widget.setReadOnly(True)
        output_widget.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #ced4da;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
            }
        """)

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

        S = S**2

        arr = []
        result_str = ""
        for j in range(min(N, 20)):
            summ = 0
            for i in range(12):
                r = random.random()
                summ += r

            x_i = summ - 6
            z_i = S * x_i + A
            arr.append(z_i)
            result_str += "{0:.4f}".format(z_i) + "  "

        self.result_text.clear()
        self.result_text.append(result_str)

        delta_1 = abs(A - self.m(arr))
        delta_2 = abs(S - self.d(arr))

        self.delta_text1.clear()
        self.delta_text2.clear()
        self.delta_text1.setText(f"{delta_1:.4f}")
        self.delta_text2.setText(f"{delta_2:.4f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
