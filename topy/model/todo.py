import datetime as dt
import os
import uuid

import click


class Todo:
    def __init__(self, name, todo_uuid=None, date=None):
        self.name = name
        if todo_uuid is None:
            self.uuid = str(uuid.uuid4())
        else:
            self.uuid = todo_uuid
        if date is None:
            self.date = str(dt.datetime.utcnow())
        else:
            self.date = date


def is_default_user_data_folder_exists():
    default_user_date_path = os.path.join(os.getenv("HOME"), ".topy")
    if not os.path.exists(default_user_date_path):
        os.mkdir(default_user_date_path)
        return False
    else:
        return True


def get_all_todos(full, last, number):
    if not is_default_user_data_folder_exists():
        return []
    else:
        all_todos = [Todo("Add a todo"), Todo("Add another todo"), Todo("Add a third todo"), Todo("Add a fourth todo")]
        if full:
            click.echo(f"return the all todos available")
        elif last:
            click.echo(f"return the last todo available")
        elif number is not None:
            click.echo(f"return the {number} todos available")
        else:
            click.echo(click.style("No argument passed", fg='red'))
        return all_todos


def add_todo(todo):
    return True


def archive_todo(clear, last, number):
    if clear:
        click.echo(f"Clear all")
    elif last:
        click.echo(f"Archive only the last todo")
    elif number:
        click.echo(f"Archive only the last {number} th todos")
    else:
        click.echo(click.style("No argument passed", fg='red'))
