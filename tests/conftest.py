import pytest
from sqlalchemy import Engine

from src.crunch import GlobalConfig, get_engine


@pytest.fixture(scope="session")
def test_configs() -> GlobalConfig:
    """Mostly exists if we need to provide test-specific support and to throw errors early."""
    return GlobalConfig()


@pytest.fixture(scope="class")
def live_engine(test_configs) -> Engine:
    return get_engine(test_configs)
