from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TodoUpdate, TodoOut

class TaskService:
    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        task = Task(**data.dict(), owner=user)
        return await task.insert()

    @staticmethod
    async def delete_task(user: User, task_id: int):
        try:
            await Task.find_one(Task.task_id == task_id).delete()
        except Exception as e:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {
                "error": e
            }

    @staticmethod
    async def update_task(user: User, data: TodoUpdate) -> Task:
        return await Task.find_one(Task.task_id == task_id).update(Task)

    @staticmethod
    async def read_task(user: User, data TodoOut) -> Task:
        return await Task.find_one(Task.task_id == task_id)