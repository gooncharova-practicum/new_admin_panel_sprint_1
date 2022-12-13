import sqlite3
import datetime

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor


import uuid
from dataclasses import dataclass, field


@dataclass
class FilmWork:
    title: str
    description: str
    creation_date: datetime.date
    rating: float = field(default=0.0)
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    # file_path


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    # postgres_saver = PostgresSaver(pg_conn)
    # sqlite_extractor = SQLiteExtractor(connection)

    # data = sqlite_extractor.extract_movies()
    # postgres_saver.save_all_data(data)


def write_to_postgres(conn: psycopg2.extensions.connection, film_work: FilmWork):
    pass


def main():
    pass


if __name__ == '__main__':
    dsl = {'dbname': 'movies_database', 'user': 'app', 'password': '123qwe', 'host': '127.0.0.1', 'port': 5432}
    with sqlite3.connect('db.sqlite') as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
