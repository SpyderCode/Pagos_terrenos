import sqlite3
from sqlite3 import Error
from datetime import datetime

def execute_sql(conn,sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def create_connection(db_file = "./database/pythonsqlite.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    execute_sql(conn,create_table_sql)

def insert_pagos(conn,date, pagos):
    sql = "INSERT INTO pagos(date, cantidad) VALUES (?,?)"

    cur = conn.cursor()
    cur.execute(sql,(date,pagos))
    conn.commit()
    return cur.lastrowid

def erase_table(conn, table):
    print("Erasing data...")
    sql = "DELETE FROM " + table +";"
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def sum_pagos(conn):
    today = datetime.today().strftime('%Y-%m-%d')
    date_start = datetime.today().replace(day=1).strftime('%Y-%m-%d')

    print("Obteniendo pagos")
    sql = f"SELECT SUM(cantidad) FROM pagos WHERE date(date) BETWEEN date('{date_start}') AND  date('{today}');"
    
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    total, = rows[0]
    print(total)
    return total