from pydantic import BaseModel

class Todo(BaseModel):
    subject: str
    title: str
    description: str
