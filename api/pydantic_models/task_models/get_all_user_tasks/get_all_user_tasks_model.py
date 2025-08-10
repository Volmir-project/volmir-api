from uuid import UUID

from pydantic import BaseModel, Field


class UserTaskModel(BaseModel):
    task_id: UUID
    task_title: str = Field(min_length=1)
    task_description: str
    task_deadline: str
    task_xp: int
    is_active: bool

class AllUserTasksModel(BaseModel):
    all_tasks: list[UserTaskModel]