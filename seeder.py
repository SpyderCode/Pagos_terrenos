import db_tools as db_tool

def main():


    sql_create_pagos_table = """CREATE TABLE IF NOT EXISTS pagos(
                                id integer PRIMARY KEY,
                                date text,
                                cantidad integer);"""

    conn = db_tool.create_connection()

    if conn is not None:

        db_tool.erase_table(conn, "pagos")
        
        print("Creating tables")
        db_tool.create_table(conn,sql_create_pagos_table)
        
        print("Done")
        
    else:
        print("ERROR: Can't connect to database.")
    


if __name__ == '__main__':
    main()



    