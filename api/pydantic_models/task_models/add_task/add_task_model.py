from uuid import UUID

from pydantic import BaseModel, Field


class AddTaskModelRequest(BaseModel):
    user_id: UUID
    task_title: str = Field(min_length=1)
    task_description: str
    task_deadline: str = Field(min_length=1)
    task_xp: int