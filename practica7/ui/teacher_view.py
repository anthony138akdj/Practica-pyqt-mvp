from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt


class TeacherView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel de Docente")
        self.resize(520, 320)

        label = QLabel(
            "Bienvenido maestro",
            alignment=Qt.AlignCenter
        )

        self.setCentralWidget(label)
