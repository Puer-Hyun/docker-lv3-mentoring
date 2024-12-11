from app.lib.restriction import develop_only
from app.route.supported_languages import service
from app.route.supported_languages.schema import SupportedLanguagesRegistrationRequest
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/supported_languages",
    tags=["supported_languages"],
    responses={404: {"description": "Not found"}},
)
