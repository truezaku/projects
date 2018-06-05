import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.exectute("CREATE TABLE IT NOT EXISTS book (id INTEGER PRIMARY KEY, tile text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    con=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.exectute("INSERT INTO book VALUES (NULL,?,?,?,?)",(tite,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    con=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.exectute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    con=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.exectute("SELECT * FROM book WHERE title=?, author=?, yea)",(tite,author,year,isbn))
    conn.commit()
    conn.close()
