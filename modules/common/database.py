import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r"C:\\Users\\User\\Desktop\\Framework\\Become-QA-Auto" + r"\\become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
