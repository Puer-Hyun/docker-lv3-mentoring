"""
Main.py works as a main function for the application
Api app starts from here
"""

from contextlib import asynccontextmanager
from logging.config import dictConfig
from os import environ

from app.lib import sample_logger
from app.route.page_contents import router as page_contents_router
from app.route.supported_languages import router as supported_languages_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url="/docs" if environ.get("DEPLOY_PHASE", "dev") == "dev" else None)

dictConfig(sample_logger)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # When app starts

    yield
    # When app teardown


app.include_router(supported_languages_router.router)
app.include_router(page_contents_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 origin 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
