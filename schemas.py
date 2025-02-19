
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    descriptional: str | None

class STask(STaskAdd):
    id: int