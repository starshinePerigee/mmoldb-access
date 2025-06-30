import pytest
from sqlalchemy.orm import Session

from src.crunch import GlobalSession


@pytest.fixture()
def live_session() -> Session:
    with GlobalSession() as session:
        yield session
