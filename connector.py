import mysql.connector
from mysql.connector import Error

class DB_Connection:
    def connect_to_db():
        try:
        # Подключение к базе данных
            connection = mysql.connector.connect(
                host='localhost',       # Замените на адрес вашего сервера
                database='TemaBuyShop',  # Замените на имя вашей базы данных
                user='root',    # Замените на имя вашего пользователя
                password='123qwE!' # Замените на пароль вашего пользователя
            )

            if connection.is_connected():
                print("Successfully connected to the database")

            # Создание курсора
                return connection
        except:
            print("Подключение не установлено.")
