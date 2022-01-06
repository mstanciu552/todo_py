from rich import print
from rich.console import Console
from rich.table import Column, Table


def help():
    help = {
        "todo <show>": "Show the todos saved",
        "todo add <name> <due_date>": "Add a todo with an optional due date",
        "todo del <id>": "Delete todo based on id",
        "todo completed <id>": "Mark a todo as completed",
    }
    print("Format [bold blue]todo <command> <arg1> <arg2>[/bold blue]")
    for key, value in enumerate(help):
        print(f"{key}\t{value}")


def format(todos):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("ID", style="dim", width=4)
    table.add_column("Todo", width=15)
    table.add_column("Due Date", justify="center", width=10)
    table.add_column("Created At", justify="center", width=10)
    table.add_column("Status", justify="center")

    for todo in todos:
        table.add_row(
            str(todo[0]), str(todo[1]), str(todo[2]), str(todo[3]), str(bool(todo[4]))
        )

    console.print(table)
