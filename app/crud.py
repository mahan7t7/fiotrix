from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app import models, schemas

async def get_task(db: AsyncSession, task_id: int) -> Optional[models.Task]:
    q = await db.execute(select(models.Task).where(models.Task.id == task_id))
    return q.scalars().first()

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[models.Task]:
    q = await db.execute(select(models.Task).offset(skip).limit(limit))
    return q.scalars().all()

async def create_task(db: AsyncSession, task_in: schemas.TaskCreate) -> models.Task:
    task = models.Task(**task_in.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def update_task(db: AsyncSession, task_id: int, task_in: schemas.TaskUpdate) -> Optional[models.Task]:
    task = await get_task(db, task_id)
    if not task:
        return None
    for field, value in task_in.dict(exclude_unset=True).items():
        setattr(task, field, value)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task_id: int) -> bool:
    task = await get_task(db, task_id)
    if not task:
        return False
    await db.delete(task)
    await db.commit()
    return True