from pydantic_settings import BaseSettings
from pydantic import BaseModel, PostgresDsn

class RunCongif(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080
    reload: bool = True

class ApiPrefix(BaseModel):
    prefix: str = '/api'

class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False 
    pool_size: int = 25

class Setting(BaseSettings):
    run: RunCongif = RunCongif()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig() 

settings = Setting()