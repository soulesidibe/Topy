import click

from topy.model.todo import Todo, add_todo, get_all_todos, archive_todo


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
    result = add_todo(todo)
    if result:
        click.echo(f"Todo created: \nName: {todo.name} \nCreated at: {todo.date} \nUuid={todo.uuid}")
    else:
        click.echo("New todo not created. Please try again. Sorry :(")


@main.command()
@click.option('--last', is_flag=True, help='Archive the last todo')
@click.option('-n', 'number', type=int, help='Archive the n first todos')
@click.option('--clear', '-c', is_flag=True, help='Archive all todos')
def archive(clear, last, number):
    """Topy menu that allows you to archive one or multiple todos"""
    archive_todo(clear, last, number)


@main.command()
@click.option("--list", '-l', 'full', is_flag=True, help="return all todos")
@click.option("--last", is_flag=True, help='return only the last todo')
@click.option("-n", 'number', type=int, help='return the n todos')
def get(full, last, number):
    """Display your todos"""
    all_todos = get_all_todos(full, last, number)
    for todo in all_todos:
        click.echo(f"{todo.name}. Created at {todo.date}\n")


if __name__ == '__main__':
    main()
