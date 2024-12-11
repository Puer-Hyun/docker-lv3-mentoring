from typing import Optional

from pydantic import BaseModel

class PageContentsRegistrationRequest(BaseModel):
    url: str
    language_id: int
    full_content: str
    summarization: Optional[str] = None
