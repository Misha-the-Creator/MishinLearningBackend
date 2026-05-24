from models.base import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Text, LargeBinary, ForeignKey
from datetime import datetime


class Articles(Base):
    __tablename__ = 'articles'

    title: Mapped[str] = mapped_column(Text)
    route: Mapped[str] = mapped_column(Text) 
    text: Mapped[str] = mapped_column(Text)
    
class PreviewImages(Base):
    __tablename__ = 'preview_images'

    image: Mapped[bytes] = mapped_column(LargeBinary)
    article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'))