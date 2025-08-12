from pydantic import BaseModel, Field


class AddPostModel(BaseModel):
    post_body: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    task_id: str = Field(min_length=1)