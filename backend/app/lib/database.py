"""Database utilities and SQLAlchemy configuration module.

This module provides utilities for database connection management and session handling
using SQLAlchemy. It includes functions for configuring the database engine,
session management, and transaction handling.

Globals:
    engine (Optional[Engine]): SQLAlchemy engine instance
    SessionMaker (Optional[scoped_session]): SQLAlchemy scoped session maker
"""

from contextlib import contextmanager
from functools import wraps
from typing import Optional

from app.lib.serializer import json_dumps
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker

__all__ = ["with_session", "engine", "configure_sqlalchemy"]

engine: Optional[Engine] = None
SessionMaker: Optional[scoped_session] = None


def configure_sqlalchemy(
    connection_uri: str,
    engine_options: Optional[dict] = None,
):
    """Configure SQLAlchemy engine and create a scoped session factory.

    Args:
        connection_uri (str): Database connection URI
        engine_options (Optional[dict]): Additional options for SQLAlchemy engine

    Returns:
        None

    Note:
        This function is idempotent - if engine is already configured, it will return early.
    """
    global engine, SessionMaker

    if engine:
        return

    options = {
        "echo": False,
        "json_serializer": lambda data: json_dumps(data, indent=None),
    }
    if engine_options:
        options.update(engine_options)
    engine = create_engine(connection_uri, **engine_options or {})
    SessionMaker = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
        ),
    )


def get_engine() -> Engine:
    """Return the configured SQLAlchemy engine instance.

    Returns:
        Engine: The configured SQLAlchemy engine

    Raises:
        Exception: If SQLAlchemy engine is not configured
    """
    global engine
    if not engine:
        raise Exception("SQLAlchemy engine is not configured.")
    return engine


def get_session_maker() -> scoped_session:
    """Return the configured SQLAlchemy scoped session maker.

    Returns:
        scoped_session: The configured session maker

    Raises:
        Exception: If SQLAlchemy session maker is not configured
    """
    global SessionMaker
    if not SessionMaker:
        raise Exception("SQLAlchemy session maker is not configured.")
    return SessionMaker


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations.

    This context manager handles the session lifecycle including commit,
    rollback in case of exceptions, and cleanup.

    Yields:
        Session: SQLAlchemy session object

    Raises:
        Exception: Any exception that occurs during the transaction

    Example:
        with session_scope() as session:
            session.query(Model).filter(Model.id == 1).first()
    """
    global SessionMaker
    session = SessionMaker()
    try:
        yield session
        session.commit()
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()


def with_session(func):
    """Handle session management for database operations.

    If a session is provided in the function arguments, uses that session.
    Otherwise, creates a new session using session_scope().

    Args:
        func: The function to wrap

    Returns:
        callable: Wrapped function that handles session management

    Example:
        @with_session
        def get_user(user_id: int, session=None):
            return session.query(User).filter(User.id == user_id).first()
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "session" in kwargs:
            return func(*args, **kwargs)
        with session_scope() as session:
            return func(*args, session=session, **kwargs)

    return wrapper
