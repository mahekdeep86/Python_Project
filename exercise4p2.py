# Mahekdeep Singh
import sqlite3
import unittest
from sqlite3 import Error

records = []


# creating connection

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


# selecting all the data from the table

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()

    # select statement
    cur.execute("SELECT * FROM canadianCheeseDirectory")

    rows = cur.fetchall()

    for row in rows:
        print(row)


"""This method is being used for testing purposes it only retrieves one row from the table"""


def select_for_testing(conn):

    # This variable is going to store that retrieved data
    global records
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()

    # Select statement to retrieve the first row from the table
    cur.execute("SELECT CheeseNameEn FROM canadianCheeseDirectory WHERE CheeseId=1")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    records.append(row)


def main():
    database = "canadianCheeseDirectory.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Mahekdeep Singh\n")
        print("All records from the table\n")
        select_all_tasks(conn)
        print("\nMahekdeep Singh")
        print("\nData testing record from database\n")
        select_for_testing(conn)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(records[0], ('test',))


if __name__ == '__main__':
    main()
    unittest.main()
