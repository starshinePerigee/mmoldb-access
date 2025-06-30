from sqlalchemy import Engine, text

from crunch import GlobalConfig
from crunch.alchemy_session import build_url, get_engine


def test_build_url():
    url = build_url(GlobalConfig())
    assert "postgresql+psycopg2:" in str(url)


def test_if_this_fails_check_your_connections():
    engine = get_engine(GlobalConfig())
    assert isinstance(engine, Engine)
    with engine.connect() as conn:
        conn.execute(text("select 'hello world'"))


def test_session_basic(live_session):
    live_session.execute(text("select 'hello world'"))
