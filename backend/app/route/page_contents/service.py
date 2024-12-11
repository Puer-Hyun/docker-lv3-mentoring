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
from app.route.page_contents.schema import PageContentsRegistrationRequest
from sqlalchemy.orm import Session

# 로깅 설정
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@with_session
def create_page_contents_record(
    body: PageContentsRegistrationRequest,
    session=None,
):
    """Create page contents record."""
    existing_page_contents = PageContentsORM.get(
        url=body.url, language_id=body.language_id, session=session
    )
    if existing_page_contents:
        existing_page_contents.update_by_dict(data=body.__dict__, session=session)
    else:
        PageContentsORM.create(**body.__dict__, session=session)
    return {"flag": "SUCCESS"}
