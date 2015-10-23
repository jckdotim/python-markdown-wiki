from app import parse_link, Topic


def test_parse_link():
    assert parse_link(u'[[Topic]]') == u'[Topic](/Topic)'


def test_topic_find(fx_session):
    topic = Topic.find('test')
    fx_session.add(topic)
    fx_session.commit()
    topic2 = Topic.find('test')
    assert topic.created_at == topic2.created_at
