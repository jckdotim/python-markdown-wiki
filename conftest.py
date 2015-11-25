from app import app, db
from pytest import fixture, yield_fixture


@fixture
def fx_app_client():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    return app.test_client()


@yield_fixture
def fx_db(fx_app_client):
    with fx_app_client:
        db.create_all()
        yield db


@fixture
def fx_session(fx_db):
    return fx_db.session
