from fastapi import APIRouter, HTTPException
from app.route.page_contents import service
from app.route.page_contents.schema import PageContentsRegistrationRequest

router = APIRouter(
    prefix="/api/page_contents",
    tags=["page_contents"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def add_page_content(register_request: PageContentsRegistrationRequest):
    """
    페이지 콘텐츠 추가
    """
    try:
        res = service.create_page_contents_record(register_request)
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
