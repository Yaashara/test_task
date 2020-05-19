import psycopg2
import pandas as pd

# Импорт конфига
from config import config

# Установка соединения с помощью вызова курсора


def create_pandas_table(sql_query):
    # Получение параметров через конфиг
    params = config()
    # Подключение к БД
    conn = psycopg2.connect(**params)
    # Создвние курсора
    cur = conn.cursor()
    # Функция обращения к БД и создания таблицы pandas

    def create_table(inner_sql_query, database=conn):
        table = pd.read_sql_query(inner_sql_query, database)
        return table

    req_table = create_table(sql_query)

    cur.close()
    conn.close()

    return req_table

# Стэк вызова для проверки работоспособности соединения и создания


if __name__ == "__main__":
    print(create_pandas_table("SELECT * FROM persons_table WHERE id=8"))
