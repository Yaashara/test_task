from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # Создание парсера
    parser = ConfigParser()
    # Считывание файла-конфигурации
    parser.read(filename)

    # Получение раздела
    db = {}

    # Проверка существования
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    # Возвращаение ошибки, если вызван параметр, которого нет в файле .ini
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


if __name__ == "__main__":
    print(config())
