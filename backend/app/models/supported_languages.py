"""
ORM for page contents and supported languages tables
"""

from app.models.base import BaseORM
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer, String, Text


class SupportedLanguagesORM(BaseORM):
    """
    지원되는 언어 정보를 저장하는 테이블
    """

    __tablename__ = "supported_languages"

    language_id = Column(Integer, primary_key=True, autoincrement=True)
    language_code = Column(String(10), nullable=False, unique=True)
    language_name = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=current_timestamp())
