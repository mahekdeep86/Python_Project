# Mahekdeep Singh
import sqlite3
from sqlite3 import Error


# To create the connection with the database

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


"""This method is being used to insert data in the table """


def create_record(conn, record):
    """
    Create a new records into the canadianCheeseDirectory table
    :param conn:
    :param record:
    :return: id
    """

    # A dynamic sql statement to insert data into the table
    sql = ''' INSERT INTO canadianCheeseDirectory(CheeseNameEn,ManufacturerNameEn,ManufacturingTypeEn,WebSiteEn)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, record)

    # here i am returning the id of the last row in which data was inserted
    return cur.lastrowid


def main():

    # name of the database
    database = "canadianCheeseDirectory.db"

    # passing name of database to the connection

    conn = create_connection(database)

    with conn:
        # Inserting data into table
        record = ('Goat Brie', 'Woolwich Dairy', 'Industrial', 'www.woolwichdairy.com')
        record_id = create_record(conn, record)


if __name__ == '__main__':
    main()
