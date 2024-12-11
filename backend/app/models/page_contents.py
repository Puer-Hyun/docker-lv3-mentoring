"""
ORM for candidates table
"""

from functools import cached_property

from app.models.base import BaseORM
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.sqltypes import Boolean, Integer, String


class PageContentsORM(BaseORM):
    """
    웹 페이지 콘텐츠 정보를 저장하는 테이블
    """

    __tablename__ = "page_contents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(2048), nullable=False)
    language_id = Column(
        Integer, ForeignKey("supported_languages.language_id"), nullable=False
    )
    full_content = Column(Text(length="MEDIUM"), nullable=False)
    summarization = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=current_timestamp())
