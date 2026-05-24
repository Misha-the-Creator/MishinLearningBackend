from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn

class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080
    reload: bool = True

class ApiPrefix(BaseModel):
    prefix: str = '/api'

class DatabaseConfig(BaseModel):
    engine: str
    user: str
    password: str
    port: int
    echo: bool = False 
    pool_size: int = 25

    def create_url(self):
        return f'postgresql+{self.engine}://{self.user}:{self.password}@localhost:{self.port}'

class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', 
                                      env_nested_delimiter='__', 
                                      case_sensitive=False)
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig

settings = Setting()