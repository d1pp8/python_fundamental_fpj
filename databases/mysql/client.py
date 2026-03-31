import pymysql
from pymysql.cursors import DictCursor
from config.config import config


class MysqlClient:
    def __init__(self):
        self.__config = config.as_dict_my_sql()

    """ A function that executes most SQL queries and returns a list of the results of the FetchALL execution. """
    def fetch_all(self, query, param=None):
        with pymysql.connect(**self.__config, cursorclass=DictCursor) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, param)
                return cursor.fetchall()

    # don't use, for latter maybe
    """ A function that performs SQL queries on data if the program needs a dictionary. """
    def fetch_one(self, query, param=None):
        with pymysql.connect(**self.__config, cursorclass=DictCursor) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, param)
                return cursor.fetchone()