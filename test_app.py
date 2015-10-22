from app import parse_link


def test_parse_link():
    assert parse_link(u'[[Topic]]') == u'[Topic](/Topic)'
