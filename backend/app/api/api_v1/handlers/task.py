from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from typing import List
from uuid import UUID
from app.schemas.task_schema import TaskCreate, TaskOut, TaskUpdate
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.models.task_model import Task
from app.services.task_service import TaskService

task_router = APIRouter()

@task_router.get('/', response_model=List[TaskOut])
async def get_tasks(current_user: User = Depends(get_current_user)):
    return await TaskService.list_task(current_user)

@task_router.get('/{task_id}')
async def get_single_task(task_id: UUID, current_user: User = Depends(get_current_user)):
    task = await TaskService.retrieve_todo(current_user, task_id)
    return task

@task_router.post('/create', response_model = Task)
async def create_tasks(data: TaskCreate, current_user: User = Depends(get_current_user)):
    return await TaskService.create_task(current_user, data)

@task_router.put('/{task_id}', response_model=TaskOut)
async def update_task(task_id: UUID, data: TaskUpdate, current_user: User = Depends(get_current_user)):
    return await TaskService.update_task(current_user, task_id, data)

@task_router.delete('/{task_id}')
async def delete_task(task_id: UUID, current_user: User = Depends(get_current_user)):
    await TaskService.delete_task(current_user, task_id)
    return None
