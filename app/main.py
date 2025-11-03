from fastapi import FastAPI
from app.routers import tasks
from app.database import engine, Base
import asyncio

app = FastAPI(title="Tasks API", version="1.0")

app.include_router(tasks.router)

# Optional: create tables on startup (simple approach; in prod use alembic)
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)