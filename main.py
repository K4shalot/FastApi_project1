from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import STaskAdd
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base is clear")
    await create_tables()
    print("base is ready to work")
    yield
    print("Turn OFF")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

class Stask(BaseModel):
    id: int
    
tasks = []

@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
    ):
    tasks.append(tasks)
    return{"ok": True}



#@app.get("/tasks")
#def get_task():
#    task = Task(name="Input this video")
#    return {"data": task}

