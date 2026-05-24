from fastapi import (APIRouter,  
                     UploadFile, 
                     Depends,
                     Form)
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_helper import db_helper
from utils.logger import logger
from db.db_manager import DBManager
from api.schemas.entities import ArticleBase, PreviewImagesBase

website_router = APIRouter(prefix='/ml',
                           tags=['website'])

@website_router.post('/post-article')
async def post_article(
    img1: UploadFile,
    img2: UploadFile,
    tex_file: UploadFile,
    title: str = Form(),
    route: str = Form(),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    
    dbmanager = DBManager(session=session)
    article = ArticleBase(title=title, route=route, tex_file=await tex_file.read())
    image = PreviewImagesBase(image_arr=[await img1.read(), await img2.read()])
    result = await dbmanager.post_article_to_db(article, image)

    return {'status': result}