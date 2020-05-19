from postgre_to_pd import create_pandas_table
import jinja2
import numpy as np
import pandas as pd


def render_without_request(template_name, **template_vars):
    """
    Функция-альтернатива для flask.render_template
    Введена для указания файла-шаблона, так как данный модуль находится вне Flask и возвращает ошибку,
    так как 'не понимает' логики архитектуры
    """
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('flask', 'templates')
        # указание на расположение __init__ файла flask, который и инициирует обращение к jinja2
    )
    template = env.get_template(template_name)
    return template.render(**template_vars)

# функция преобразование в html-страницу полного списка записей в БД

def req_get():
    df = create_pandas_table("SELECT name, surname FROM persons_table")
    return render_without_request('simple.html',  tables=[df.to_html(index=False)], titles=df.columns.values)

# Функция преобразования в html-страницу одной строки БД

def req_get_id(name_id):
    df = create_pandas_table("SELECT name, surname FROM persons_table WHERE id={}".format(name_id))
    return render_without_request('simple.html',  tables=[df.to_html(index=False)], titles=df.columns.values)


if __name__ == '__main__':
    print(req_get_id(2))
