from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate

class TaskService:
    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        task = Task(**data.dict(), owner=user)
        return await task.insert()