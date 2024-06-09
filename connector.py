import mysql.connector
import logging
import configure
from mysql.connector import Error

class DB_Connection:
    def connect_to_db():
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename='connector.log', level=logging.INFO)

        try:
        # Подключение к базе данных
            connection = mysql.connector.connect(
                host='localhost',
                database='TemaBuy',
                user='root',
                password='ser0905mama'
            )

            if connection.is_connected():
                logger.info("Успешное подключение к базе данных.")

            # Возврат курсорса
                return connection
        except:
            logger.error("Не удалось подключиться к базе данных.")
