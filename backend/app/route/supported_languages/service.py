"""
Page contents service.
Functions handling business logic should be defined here.
DB operations should be defined in models.
Complicate or multiple ORM operations should be done here
"""

import logging

from app.lib.database import with_session
from app.lib.response import as_dict
from app.models.page_contents import PageContentsORM
from app.route.supported_languages.schema import SupportedLanguagesRegistrationRequest
from sqlalchemy.orm import Session

# 로깅 설정
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
