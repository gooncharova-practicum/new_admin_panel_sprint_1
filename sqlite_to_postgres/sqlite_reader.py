import sqlite3
from logging import getLogger


class SQLiteExtractor:
    def __init__(self, connection) -> None:
        self.cursor = connection.cursor()
        self.logger = getLogger()

    def get_data(self, db_table):
        query = f'SELECT * FROM {db_table};'
        data = {}

        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()

        except sqlite3.DatabaseError as err:
            self.logger.error(err)

        self.logger.debug(f'Extract data is over. Get {len(data)} from table {db_table}')
        return data
