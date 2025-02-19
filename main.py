from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_table
from router import router as tasks_router

@asynccontextmanager
async def lifespan(age: FastAPI):
    await delete_table()
    print("База очищена")
    await create_table()
    print("База готова")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



