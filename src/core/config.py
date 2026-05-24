from pydantic_settings import BaseSettings
from pydantic import BaseModel

class RunCongif(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000
    reload: bool = True

class ApiPrefix(BaseModel):
    prefix: str = '/api'

class Setting(BaseSettings):
    run: RunCongif = RunCongif()
    api: ApiPrefix = ApiPrefix()
    db_url: str

settings = Setting()