from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from db.models.tables.articles import Articles, PreviewImages
from utils.logger import logger


class DBManager:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def post_article_to_db(self, insert_dict: dict):
        try:
            stmt = (select(Articles).where(insert_dict['title']))
            result = await self.session.execute(stmt)
            row = result.scalars().all()

            if row:
                return 'Строка с таким title уже содержится в таблице articles'

            stmt = (insert(Articles).values(**insert_dict))
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        
        except Exception as e:
            logger.error(f'Ошибка при добавлении в atricles: {e}')
            return False