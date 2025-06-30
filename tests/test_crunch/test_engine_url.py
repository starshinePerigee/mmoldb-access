from sqlalchemy import Engine

from crunch.alchemy_engine import build_url


def test_if_this_fails_check_your_connections(live_engine):
    assert isinstance(live_engine, Engine)


def test_build_url(test_configs):
    url = build_url(test_configs)
    assert "postgresql+psycopg2:" in str(url)
