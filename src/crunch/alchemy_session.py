from sqlalchemy import URL, Engine, create_engine
from sqlalchemy.orm import Session

from crunch import GlobalConfig


def build_url(config: GlobalConfig) -> URL:
    db_config = config["connection"]
    return URL.create(
        drivername="postgresql+psycopg2",
        username=db_config["username"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config["port"],
        database="mmoldb",
    )


def get_engine(config: GlobalConfig) -> Engine:
    engine = create_engine(url=build_url(config), echo=config["connection"]["echo"])
    return engine


class GlobalSession:
    """
    A session object with context manager support that use a global singleton Engine
    """

    _engine = None

    def __init__(self):
        if GlobalSession._engine is None:
            GlobalSession._engine = get_engine(GlobalConfig())
        self._session = None

    def __enter__(self):
        self._session = Session(GlobalSession._engine)
        return self._session.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._session.__exit__(exc_type, exc_val, exc_tb)
