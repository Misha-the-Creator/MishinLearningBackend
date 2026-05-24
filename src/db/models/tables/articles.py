from db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, LargeBinary, ForeignKey


class Articles(Base):
    __tablename__ = 'articles'

    title: Mapped[str] = mapped_column(Text)
    route: Mapped[str] = mapped_column(Text) 
    tex_file: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)
    
class PreviewImages(Base):
    __tablename__ = 'preview_images'

    image: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)
    article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'))