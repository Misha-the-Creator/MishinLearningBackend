import uvicorn
from db.db_helper import db_helper
from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # app startup
    yield
    # app shutdown
    print('Шатдаун')
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

def main():
    print("Hello from ml-back!")


if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=settings.run.reload)
