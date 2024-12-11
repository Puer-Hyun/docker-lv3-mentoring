from app.lib.restriction import develop_only
from app.route.page_contents import service
from app.route.page_contents.schema import PageContentsRegistrationRequest
from fastapi import APIRouter, HTTPException, Request

router = APIRouter(
    prefix="/api/page_contents",
    tags=["page_contents"],
    responses={404: {"description": "Not found"}},
)
