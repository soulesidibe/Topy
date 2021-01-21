import datetime as dt
import uuid

import click


class Todo:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.date = str(dt.datetime.utcnow())


@click.group()
@click.version_option("0.1.0")
def main():
    """This is the help page of Topy"""
    pass


@main.command()
@click.argument('todo_name')
def new(todo_name):
    """Add a todo to Topy"""
    todo = Todo(todo_name)
    click.echo(
        f"Hello man you just created a new todo: \nName: {todo.name} \nCreated at: {todo.date} \nUuid={todo.uuid}")


@main.command()
@click.option('--last', is_flag=True, help='Archive the last todo')
@click.option('-n', 'number', type=int, help='Archive the n first todos')
@click.option('--clear', '-c', is_flag=True, help='Archive all todos')
def archive(clear, last, number):
    """Topy menu that allows you to archive one or multiple todos"""
    pass


@main.command()
@click.option("--list", '-l', 'full', is_flag=True, help="return all todos")
@click.option("--last", is_flag=True, help='return only the last todo')
@click.option("-n", 'number', type=int, help='return the n todos')
def get(full, last, number):
    """Display your todos"""
    if full:
        click.echo(f"return the all todos available")
    elif last:
        click.echo(f"return the last todo available")
    elif number is not None:
        click.echo(f"return the {number} todos available")
    else:
        click.echo(click.style("No argument passed", fg='red'))


if __name__ == '__main__':
    main()
