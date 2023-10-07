from uuid import UUID, uuid4
from datetime import datetime
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from typing import List
from .user_model import User

class Task(Document):
    task_id: UUID = Field(default_factory = uuid4)
    title: str = Field(..., title="Name of the task.", max_length=100)
    description: str = Field(..., title="Description of the task.", max_length=500)
    estimated_time: int
    status: str | None = Field(..., title = "Task Status")
    pomodoro_config: List = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name = 'task'
