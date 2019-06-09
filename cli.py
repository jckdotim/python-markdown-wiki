import click
from app import db


@click.group()
def cli():
    pass


@click.command()
def createdb():
    db.create_all()


@click.command()
def dropdb():
    db.drop_all()


cli.add_command(createdb)
cli.add_command(dropdb)


if __name__ == '__main__':
    cli()
