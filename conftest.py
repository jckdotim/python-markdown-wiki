from app import app, db
from pytest import fixture, yield_fixture


@fixture
def fx_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    yield app


@fixture
def fx_app_client(fx_app):
    return fx_app.test_client()


@yield_fixture
def fx_db(fx_app):
    with fx_app.app_context():
        db.create_all()
        yield db


@fixture
def fx_session(fx_db):
    return fx_db.session
