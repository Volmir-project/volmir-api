from pydantic import BaseModel, Field


class SignupModelRequest(BaseModel):
    email: str = Field(min_length=1)
    username: str = Field(min_length=1)
    password1: str = Field(min_length=1)
    password2: str = Field(min_length=1)