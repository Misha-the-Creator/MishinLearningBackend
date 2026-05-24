from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from db.models.tables.articles import Articles, PreviewImages
from utils.logger import logger
from api.schemas.entities import ArticleBase, PreviewImagesBase


class DBManager:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def post_article_to_db(self, article: ArticleBase, images: PreviewImagesBase):
        try:
            stmt = (select(Articles).where(Articles.title == article.title))
            result = await self.session.execute(stmt)
            row = result.scalars().all()
            
            if row:
                return 'Строка с таким title уже содержится в таблице articles'
            
            stmt = (insert(Articles).values(article.__dict__))
            await self.session.execute(stmt)
            await self.session.commit()

            stmt = (select(Articles.id).where(Articles.title == article.title))
            result = await self.session.execute(stmt)
            title_id = result.scalar_one()
            images.article_id = title_id

            for image in images.image_arr:
                insert_image = {'image': image,
                                'article_id': images.article_id}
                stmt = (insert(PreviewImages).values(insert_image))
                await self.session.execute(stmt)
                
            await self.session.commit()
            return True
        
        except Exception as e:
            logger.error(f'Ошибка при добавлении в articles и images: {e}')
            return False