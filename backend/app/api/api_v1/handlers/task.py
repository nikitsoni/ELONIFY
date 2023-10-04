from fastapi import APIRouter, Depends
from app.schemas.task_schema import TaskCreate
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.models.task_model import Task
from app.services.task_service import TaskService

task_router = APIRouter()

@task_router.post('/create')
async def create_tasks(data: TaskCreate, current_user: User = Depends(get_current_user)):
    return await TaskService.create_task(current_user, data)