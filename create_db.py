import sqlite3


def create_db():
    con = sqlite3.connect('site_db.sqlite')
    cur = con.cursor()
    with open('create_db.sql', 'r') as f:
        text = f.read()
    cur.executescript(text)
    cur.close()
    con.close()


if __name__ == "__main__":
    create_db()
