from uuid import UUID

from pydantic import BaseModel

class Task(BaseModel):
    task_id: UUID
    task_title: str
    task_description: str
    task_deadline: str
    is_active: bool
    task_xp: int

class Comment(BaseModel):
    comment_creator: str
    comment_content: str

class GetAllPostsModel(BaseModel):
    linked_task: Task
    full_name: str
    post_body: str
    postLikesCount: int
    postComments: list[Comment]
