from utils import format
from migrations.db import Database

db = Database()
db.create()


def show():
    todos = db.select("todos")
    if len(todos) == 0:
        print("No todos to display")
        return
    format(todos)


def add(todo: str, due_date: str = None):
    fields = {
        "todo": todo,
        **({"due_date": str(due_date)} if due_date else {}),
    }
    db.insert("todos", fields)
    print(f"Task {todo} added")


def deltodo(id: str):
    db.delete("todos", int(id))
    print(f"Task with id {id} deleted")


def completed(id: str):
    db.update("todos", {"completed": 1}, id)
    print(f"Task with id {id} completed")
