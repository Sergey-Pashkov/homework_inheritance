# Проект: Система управления пользователями с использованием наследования

Этот проект демонстрирует систему управления пользователями с использованием наследования и отслеживания сессий. Он разработан для онлайн-платформы с разными ролями пользователей (Клиент и Администратор).

## Структура
- **User**: Базовый класс для пользователей, с функциями хеширования и проверки пароля.
- **Customer**: Производный от User класс, представляющий обычного пользователя.
- **Admin**: Производный от User класс, с дополнительными правами для управления пользователями.
- **AuthenticationService**: Управляет регистрацией, входом, выходом и отслеживанием сессий пользователей.

## Функции
1. Регистрация пользователей с проверкой уникальности имени и хешированием паролей.
2. Аутентификация пользователей с проверкой пароля.
3. Управление сессиями для отслеживания текущего пользователя.
4. Функции для администратора: просмотр и удаление пользователей.

## Использование
Для запуска программы выполните:
```bash
python shop.py
