from pydantic import BaseModel


class UserCardDataResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    xp: int