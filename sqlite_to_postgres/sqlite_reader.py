class SQLiteExtractor:
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_data(self, db_table):
        query = f'SELECT * FROM {db_table};'
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return dict(data[0])
