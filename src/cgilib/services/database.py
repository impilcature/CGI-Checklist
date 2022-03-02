"""
This module supports the following schema:





"""

import sqlite3


class DatabaseManager:
    def __init__(self, database_filename) -> None:
        # added this to persist the name of the database file
        self.database_filename = database_filename
        self.connection = sqlite3.connect(database_filename)

    def __del__(self):
        self.connection.close()