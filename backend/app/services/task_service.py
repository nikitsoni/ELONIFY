from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskOut

class TaskService:
    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        task = Task(**data.dict(), owner=user)
        return await task.insert()

    @staticmethod
    async def delete_task(user: User, task_id: UUID) -> None:
        task = await TaskService.retrieve_todo(user, task_id)
        if task:
            await task.delete()
        return None

    @staticmethod
    async def update_task(user: User, task_id: UUID, data: TaskUpdate) -> Task:
        task = await TaskService.retrieve_todo(user, task_id)
        await task.update({"$set": data.dict(exclude_unset=True)})
        
        await task.save()
        return task

    @staticmethod
    async def list_task(user: User) -> List[Task]:
        return await Task.find(Task.owner.id == user.id).to_list()

    @staticmethod
    async def retrieve_todo(user: User, task_id: UUID):
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        return task