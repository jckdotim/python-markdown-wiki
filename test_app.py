from app import parse_link, Topic


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
