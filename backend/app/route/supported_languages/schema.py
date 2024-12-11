from typing import Optional

from pydantic import BaseModel


class SupportedLanguagesRegistrationRequest(BaseModel):
    language_code: str
    language_name: str
