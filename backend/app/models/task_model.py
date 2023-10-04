from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field
from typing import List

class Task(Document):
    task_id: UUID = Field(default_factory = uuid4)
    title: str = Field(..., title="Name of the task.", max_length=100)
    description: str = Field(..., title="Description of the task.", max_length=500)
    estimated_time: int
    status: str | None = Field(..., title = "Task Status")
    pomodoro_config: List = []

    class Settings:
        name = 'task'
