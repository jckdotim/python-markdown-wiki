import uuid

from app import parse_link, Topic
from flask import url_for


def test_parse_link():
    assert parse_link(u'[[Topic]]') == u'[Topic](/Topic)'


def test_topic_find(fx_session):
    topic = Topic.find('test')
    fx_session.add(topic)
    fx_session.commit()
    topic2 = Topic.find('test')
    assert topic.created_at == topic2.created_at


def test_backlinks(fx_session):
    foo = Topic.find('foo')
    bar = Topic.find('bar')
    bar.body = ''
    fx_session.add(foo)
    fx_session.add(bar)
    fx_session.commit()
    assert foo.backlinks.count() == 0
    bar.body = 'test for [[foo]]'
    fx_session.commit()
    assert foo.backlinks.count() == 1
    assert foo.backlinks[0] == bar


def test_redirect_to_readme(fx_app_client):
    with fx_app_client as app:
        assert app.get('/').location == url_for(
            'topic',
            topic=Topic.find('README')
        )


def test_search(fx_app_client):
    with fx_app_client as app:
        assert app.get('/?topic=TEST').location == url_for(
            'topic',
            topic=Topic.find('TEST')
        )


def test_200(fx_app_client):
    urls = [
        '/README',
        '/README/backlinks',
        '/README/edit',
        '/README/keynote'
    ]
    with fx_app_client as app:
        for url in urls:
            assert app.get(url).status_code == 200


def test_edit_topic(fx_app_client):
    with fx_app_client as app:
        test_body = str(uuid.uuid4())
        rv = app.post('/README', data=dict(
            body=test_body
        ), follow_redirects=True)
        assert test_body in str(rv.data)
