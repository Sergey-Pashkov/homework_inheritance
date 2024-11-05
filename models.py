import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        User.users.append(self)

    @staticmethod
    def hash_password(password):
        """
        Хеширует пароль с использованием UUID для усиления безопасности.
        """
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля путем сравнения хешей.
        """
        password, salt = stored_password.split(':')
        return password == hashlib.sha256(salt.encode() + provided_password.encode()).hexdigest()

    def get_details(self):
        """
        Возвращает информацию о пользователе.
        """
        return f"User: {self.username}, Email: {self.email}"


class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        """
        Возвращает информацию о клиенте.
        """
        return f"Customer: {self.username}, Email: {self.email}, Address: {self.address}"


class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        """
        Возвращает информацию об администраторе.
        """
        return f"Admin: {self.username}, Email: {self.email}, Level: {self.admin_level}"

    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        return [user.get_details() for user in User.users]

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """
        User.users = [user for user in User.users if user.username != username]


class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    def __init__(self):
        self.current_user = None

    def register(self, user_class, username, email, password, *args):
        """
        Регистрация нового пользователя.
        """
        if any(user.username == username for user in User.users):
            raise ValueError("Username already exists.")
        return user_class(username, email, password, *args)

    def login(self, username, password):
        """
        Аутентификация пользователя.
        """
        for user in User.users:
            if user.username == username and User.check_password(user.password, password):
                self.current_user = user
                return f"{username} logged in successfully."
        raise ValueError("Invalid username or password.")

    def logout(self):
        """
        Выход пользователя из системы.
        """
        self.current_user = None
        return "Logged out successfully."

    def get_current_user(self):
        """
        Возвращает текущего вошедшего пользователя.
        """
        if self.current_user:
            return self.current_user.get_details()
        return "No user currently logged in."
