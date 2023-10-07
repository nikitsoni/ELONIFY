from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from app.schemas.task_schema import TaskCreate, TodoOut, TodoUpdate
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.models.task_model import Task
from app.services.task_service import TaskService

task_router = APIRouter()

@task_router.get('/')
async def get_tasks(data: TodoOut, current_user: User = Depends(get_current_user))

@task_router.post('/create')
async def create_tasks(data: TaskCreate, response_model = TaskCreate, current_user: User = Depends(get_current_user)):
    return await TaskService.create_task(current_user, req.data)

@task_router.delete('/delete/{task_id}')
async def delete_task(data, current_user: User = Depends(get_current_user)):
    return await TaskService.delete_task(current_user, data.task_id)

@task.task_router.put('/update/{task_id}')
async def update_task(data: TodoUpdate, req: TodoUpdate = Body(...), current_user: User = Depends(get_current_user)):
    return await TaskService.update_task(current_user, req.data)
