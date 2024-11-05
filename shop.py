from models import User, Customer, Admin, AuthenticationService

# Создаем экземпляр AuthenticationService для управления сессиями
auth_service = AuthenticationService()

# Пример регистрации и авторизации пользователей
# Регистрация пользователя-клиента
auth_service.register(Customer, "alice", "alice@example.com", "password123", "123 Main St")
auth_service.register(Admin, "admin", "admin@example.com", "adminpass", 1)

# Попытка входа пользователя
print(auth_service.login("alice", "password123"))
print("Current User:", auth_service.get_current_user())

# Выход пользователя
print(auth_service.logout())

# Вход администратора
print(auth_service.login("admin", "adminpass"))

# Проверка списка пользователей для админа
print("Users List:", Admin.list_users())

# Удаление пользователя (только для админа)
Admin.delete_user("alice")
print("Users List after deletion:", Admin.list_users())

# Проверка текущего пользователя
print("Current User:", auth_service.get_current_user())
