"""
models classes for sqlalchemy orm
"""

from app.lib.database import engine

print(engine)
from .page_contents import *
from .supported_languages import *

PageContentsORM.metadata.create_all(engine)
SupportedLanguagesORM.metadata.create_all(engine)
