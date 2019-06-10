import click
from app import db


@click.group()
def cli():
    pass


@cli.command()
def createdb():
    db.create_all()


@cli.command()
def dropdb():
    db.drop_all()


if __name__ == '__main__':
    cli()
