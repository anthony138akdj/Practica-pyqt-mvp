# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self, valid_user: str = "admin", valid_password: str = "1234"):
        self._user = valid_user
        self._password = valid_password

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        users = {
            "admin":("1234", "admin"),
            "estudiante":("1234","student"),
            "maestro":("1234","teacher"),
        }
        if username in users and password == users[username][0]:
            role = users[username][1]
            return AuthResult(True, "Autenticación exitosa.", role)
        return AuthResult(False, "Usuario o contraseña incorrectos.")
