from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict

class STaskAdd(BaseModel):
    name: str
    description: str | None
    
class STask(STaskAdd):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
    
class STaskId(BaseModel):
    ok: bool = True
    task_id: int