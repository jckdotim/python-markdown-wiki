import click
from app import app, db


@click.group()
def cli():
    pass


@cli.command()
def createdb():
    with app.app_context():
        db.create_all()


@cli.command()
def dropdb():
    with app.app_context():
        db.drop_all()


if __name__ == '__main__':
    cli()
