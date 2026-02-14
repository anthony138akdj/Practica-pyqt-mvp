# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter
from ui.student_view import StudentView
from ui.teacher_view import TeacherView


class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_ADMIN = 1
    PAGE_STUDENT = 2
    PAGE_TEACHER = 3

    def __init__(self):
        super().__init__()

        self.login_view = LoginView()
        self.main_view = MainView()
        self.student_view = StudentView()
        self.teacher_view = TeacherView()

        


        self.auth_service = AuthService()
        
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_main
        )
        self.addWidget(self.login_view)
        self.addWidget(self.main_view)
        self.addWidget(self.student_view)
        self.addWidget(self.teacher_view)
        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(640, 400)

    def _go_main(self, username: str, role : str):
        
        if role == "admin":
           
           self.setCurrentIndex(self.PAGE_ADMIN)

        elif role == "student" :
            self.setCurrentIndex(self.PAGE_STUDENT)

        elif role == "teacher":
            self.setCurrentIndex(self.PAGE_TEACHER)
        else:
            self.setCurrentIndex(self.PAGE_LOGIN)
            
