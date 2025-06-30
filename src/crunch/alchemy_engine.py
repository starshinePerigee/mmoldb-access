from sqlalchemy import URL, Engine, create_engine, text

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
    
    with engine.connect() as conn:
        conn.execute(text("select 'hello world'"))
    
    return engine
