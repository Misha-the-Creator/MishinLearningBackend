from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    route: str
    text: str

class PreviewImagesBase(BaseModel):
    image: bytes
    article_id: int