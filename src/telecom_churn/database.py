"""MySQL connection helpers."""

from __future__ import annotations

from sqlalchemy import Engine, create_engine
from sqlalchemy.engine import URL

from .config import DatabaseConfig


def create_mysql_engine(config: DatabaseConfig | None = None) -> Engine:
    """Create a SQLAlchemy engine without exposing credentials in source code."""
    settings = config or DatabaseConfig.from_environment()
    url = URL.create(
        drivername="mysql+pymysql",
        username=settings.user,
        password=settings.password,
        host=settings.host,
        port=settings.port,
        database=settings.database,
    )
    return create_engine(url, pool_pre_ping=True)
