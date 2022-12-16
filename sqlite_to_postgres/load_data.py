import os
import sqlite3

import psycopg2

from contextlib import contextmanager
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from .write_data import write_to_postgres
from .sqlite_reader import SQLiteExtractor
from movies_admin.movies.models import __all__ as models


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    sqlite_reader = SQLiteExtractor(connection)
    # postgres_saver = PostgresSaver(pg_conn)

    for model in models:
        data = sqlite_reader.get_data(model)
        write_to_postgres(data)


if __name__ == '__main__':
    dsl = {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'host': os.environ.get('DB_HOST', '127.0.0.1'),
        'port':  os.environ.get('DB_PORT', 5432),
    }
    db_path = os.environ.get('DB_PATH', 'db.sqlite')
    with (conn_context(db_path) as sqlite_conn,
            psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn):
        load_from_sqlite(sqlite_conn, pg_conn)
