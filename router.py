from schemas import STask, STaskAdd, STaskId
from fastapi import Depends, FastAPI, APIRouter
from typing import Annotated, Optional
from repository import TaskRepository




router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)



@router.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
    )-> STaskId:
    task_id = await TaskRepository.add_one(task)
    return{"ok": True, "task_id": task_id}



@router.get("")
async def get_task() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks