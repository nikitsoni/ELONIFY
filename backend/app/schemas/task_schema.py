from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    description: str = Field(..., title='Description', max_length=755, min_length=1)
    estimated_time: str
    status: Optional[bool] = False
    pomodoro_config: Optional[List] = [25, 5, 10]


class TaskUpdate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    description: str = Field(..., title='Description', max_length=755, min_length=1)
    estimated_time: str
    status: Optional[bool] = False
    pomodoro_config: List = [25, 5, 10]
    

class TaskOut(BaseModel):
    task_id: UUID
    status: bool
    title: str
    description: str
    estimated_time: str
    pomodoro_config: List
    created_at: datetime
    updated_at: datetime