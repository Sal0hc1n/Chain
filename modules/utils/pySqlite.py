'''
pySqlite.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.0
@date: 14/06/17
@status: WRK
'''

import os
import sqlite3


class Tools(object):
    """docstring for tools."""

    def __init__(self):
        pass

    # from list to dictionary
    def fetchOneAssoc(self, cursor):
        data = cursor.fetchone()
        if data is None:
            return None

        desc = cursor.description

        dictionary = {}

        for (name, value) in zip(desc, data):
            dictionary[name[0]] = value

        return dictionary


class pySqlite3(object):
    def __init__(self):
        # pySqlite3.py path
        dir = os.path.dirname(__file__)

        # full db path
        db_path = os.path.join(dir, '../../data/database.db')

        # connection obkect
        self.db = sqlite3.connect(db_path)

        # cursor to execute query
        self.cursor = self.db.cursor()

        # tools object
        self.tools = Tools()

    # close db connection
    def close_db(self):
        self.conn.close()

    # runs a query
    def execute(self, query, args=None):  # Lancia query
        if args is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, args)

    # Runs a query and checks that it had a good end
    def execute_check(self, query, args=None, ok_message=None):
        try:
            # runs query
            if args is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, args)

            # commit changes
            self.db.commit()

            if ok_message is not None:
                print(ok_message)

            return True
        except sqlite3.Error as e:
            # if error, rollback
            self.db.rollback()

            print("An error occurred:", e.args[0])

            return False

    # Runs a query, checks that it had a good end and returns the result as a list of lists
    def execute_check_fetch_list(self, query, args=None, ok_message=None):
        if self.execute_check(query, args, ok_message):
            result = []

            fetch = list(self.cursor.fetchone())

            while True:
                result.append(fetch)
                fetch = self.cursor.fetchone()
                if fetch is None:
                    break
                else:
                    fetch = list(fetch)

            return result  # list of lists
        else:
            return None

    # Runs a query, checks that it had a good end and returns the result as a list of dictionaries
    def execute_check_fetch_dict(self, query, args=None, ok_message=None):
        if self.execute_check(query, args, ok_message):
            result = []

            fetch = self.tools.fetchOneAssoc(self.cursor)

            while True:
                result.append(fetch)
                fetch = self.tools.fetchOneAssoc(self.cursor)
                if fetch is None:
                    break

            return result  # list of dictionaries

        else:
            return None


'''
db = pySqlite3()
query = 'SELECT * FROM Action'
print(db.execute_check_fetch_dict(query))
'''
