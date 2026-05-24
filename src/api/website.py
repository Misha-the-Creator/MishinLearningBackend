from typing import Annotated
from fastapi import (APIRouter, 
                     File, 
                     UploadFile, 
                     Depends)
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_helper import db_helper
from db.db_manager import DBManager
from utils.logger import logger
from api.schemas.entities import ArticleBase, PreviewImagesBase

website_router = APIRouter(prefix='/ml',
                           tags=['website'])

@website_router.post('/post-article')
async def post_article(insert_dict: ArticleBase,
                       img1: UploadFile,
                       img2: UploadFile,
                       session: AsyncSession = Depends(db_helper.session_getter)):
    
    dbmanager = DBManager(session=session)

    result = await dbmanager.post_article_to_db(insert_dict)

    return {'status': result}