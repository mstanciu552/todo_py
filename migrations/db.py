#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error

PATH = "migrations/db/db.sqlite"


class Database:
    def __init__(self, path: str = None):
        self.path = path if path else PATH
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Database Error: {e}")

    def create(self):
        if self.check_table("todos"):
            return
        create_todo_table = f"""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY NOT NULL,
                todo TEXT NOT NULL,
                due_date DATE DEFAULT NULL,
                created_at DATE DEFAULT (date('now')),
                completed BOOL DEFAULT FALSE
            );
        """
        self.exec_query(create_todo_table)
        print("Created table TODOS")

    def check_table(self, table: str):
        query = f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}'"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0] == 1

    def select(self, table: str, id: int = None):
        query = f"SELECT * FROM {table}"
        if id:
            query += f" WHERE id={id}"
        query += ";"

        self.exec_query(query)
        return self.cursor.fetchall()

    def insert(self, table: str, data: dict):
        if not data:
            raise Error("Wrong data format")

        fields = ""
        values = "'"
        for key, value in data.items():
            fields += key + ","
            values += str(value) + "','"

        fields = fields[: len(fields) - 1]
        values = values[: len(values) - 2]

        query = f"INSERT INTO {table}({fields}) VALUES({values})"

        self.exec_query(query)

    def delete(self, table: str, id: int):
        if not id:
            return

        delete_query = f"""
            DELETE FROM {table} 
            WHERE id = {str(id)}
        """
        self.cursor.execute(delete_query)
        self.connection.commit()

    def update(self, table: str, data: dict, id: str):
        if not data or table == "":
            return
        query = f"UPDATE {table} SET "
        for key, value in data.items():
            query += f'{key} = "{value}",'
        query = query[:-1]
        query += f" WHERE id={id};"

        self.exec_query(query)

    def exec_query(self, query: str):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print(f"Query Error: {e}")
