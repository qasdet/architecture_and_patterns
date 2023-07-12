import sqlite3
from framework.common import *


def create_db():
    con = sqlite3.connect(DB_name)
    cur = con.cursor()
    with open(FILE_CREATE_DATABASE_COMMAND) as f:
        text = f.read()
    cur.executescript(text)
    cur.close()
    con.close()


if __name__ == "__main__":
    create_db()
