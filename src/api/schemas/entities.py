from pydantic import BaseModel
from typing import List

class ArticleBase(BaseModel):
    title: str
    route: str
    tex_file: bytes

class PreviewImagesBase(BaseModel):
    article_id: int | None = None
    image_arr: List[bytes]