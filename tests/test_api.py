

from starfighter.api import API


def test_heartbeat():
    api = API()
    assert api.heartbeat()
    assert not api.heartbeat(.0001)


def test_venue_heartbeat():
    api = API()
    assert api.venue_heartbeat('TESTEX')
    assert not api.venue_heartbeat('TESTEX', .0001)


def test_stocks():
    api = API()
    r = api.stocks('TESTEX')
    print r
    assert r[0]['symbol'] == 'FOOBAR'


def test_order():
    api = API('EXB123456')
    r = api.order('TESTEX', 'FOOBAR', 0, 100, 'buy', 'limit')
    assert r['ok']