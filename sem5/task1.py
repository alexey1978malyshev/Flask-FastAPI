"""📌 Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс Task с полями id, title, description и status.
📌 Создайте список tasks для хранения задач.
📌 Создайте маршрут для получения списка задач (метод GET).
📌 Создайте маршрут для создания новой задачи (метод POST).
📌 Создайте маршрут для обновления задачи (метод PUT).
📌 Создайте маршрут для удаления задачи (метод DELETE).
📌 Реализуйте валидацию данных запроса и ответа."""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import logging
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="Flask-FastAPI/sem5/ templates")


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = None


task_1 = Task(id=1, title="test1", description="desc_test1", status="disable")
task_2 = Task(id=2, title="test2", description="desc_test2", status="enable")
tasks = [task_1, task_2]


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "Seminar 5"}


@app.get("/tasks")
async def read_task(request: Request):
    logger.info(f'Отработал GET запрос для tasks')
    return {"tasks": tasks}


@app.post("/tasks/")
async def create_task(task: Task):
    logger.info('Отработал POST запрос создания новой задачи.')
    tasks.append(task)
    return task


@app.put("/tasks/{tasks_id}")
async def update_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
    logger.info(f'Отработал PUT запрос для task id = {task}')
    return task


@app.delete("/tasks/{tasks_id}")
async def delete_item(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks.remove(tasks[i])
    logger.info(f'Отработал DELETE запрос для task_id = {task_id}.')
    #return {"item_id": item_id}
