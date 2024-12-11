from os import environ

from app.lib.database import configure_sqlalchemy

_db_uri = (
    environ.get("DATABASE_URL")
    or f"mysql+pymysql://{environ['MYSQL_USER']}:{environ['MYSQL_PASSWORD']}@{environ['MYSQL_HOST']}:3306/{environ['MYSQL_DATABASE']}"
)


configure_sqlalchemy(
    connection_uri=_db_uri,
    engine_options={
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 3600,
    },
)
