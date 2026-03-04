from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int

    class Config:
        from_attributes = True