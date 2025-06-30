from crunch.access_config import GlobalConfig


def test_globalconfig_init():
    cfg = GlobalConfig()
    assert isinstance(cfg["connection"]["host"], str)
    assert isinstance(cfg["connection"]["port"], int)
