from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine
from sqlalchemy.orm import sessionmaker

from models.settings import settings


def create_pyodbc_engine(isolation_level: str = "READ COMMITTED") -> Engine:
    connection_url = URL.create(
        "mssql+pyodbc",
        **settings.DB_SQLSERVER.dict(),
        **settings.DB_USER.dict(),
        database=settings.HR_DB_NAME,
        query={
            "driver": "ODBC Driver 18 for SQL Server",
            "Encrypt": "YES",
            "TrustServerCertificate": "YES",
            "charset": "utf8",
        },
    )

    engine = create_engine(
        connection_url,
        max_overflow=settings.DB_Config.DB_POOL_MAX_OVERFLOW,
        pool_pre_ping=True,
        # echo=True,
        pool_timeout=60,
        pool_size=settings.DB_Config.DB_POOL_SIZE,
        isolation_level=isolation_level,
    )
    return engine


partner_engine_read_uncommitted = create_pyodbc_engine(
    isolation_level="READ UNCOMMITTED"
)

SessionReadUncommitted = sessionmaker(
    bind=partner_engine_read_uncommitted,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False,
)
