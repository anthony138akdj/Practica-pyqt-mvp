from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt


class StudentView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel de Estudiante")
        self.resize(520, 320)

        label = QLabel(
            "Bienvenido estudiante",
            alignment=Qt.AlignCenter
        )

        self.setCentralWidget(label)
