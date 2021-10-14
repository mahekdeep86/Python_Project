import unittest
import os
import sqlite3
from sqlite3 import Error
import exercise4p2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        exercise4p2.select_for_testing(conn)
        result = exercise4p2.select_for_testing()
        self.assertEqual(result, "test")


if __name__ == '__main__':
    unittest.main()
