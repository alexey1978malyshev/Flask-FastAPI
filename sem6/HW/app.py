"""📌 Напишите API для управления списком задач. Для этого создайте модель Task
со следующими полями:
○ id: int (первичный ключ)
○ title: str (название задачи)
○ description: str (описание задачи)
○ done: bool (статус выполнения задачи)
📌 API должно поддерживать следующие операции:
○ Получение списка всех задач: GET /tasks/
○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
○ Создание новой задачи: POST /tasks/
○ Обновление информации о задаче: PUT /tasks/{task_id}/
○ Удаление задачи: DELETE /tasks/{task_id}/
📌 Для валидации данных используйте параметры Field модели Task.
📌 Для работы с базой данных используйте SQLAlchemy и модуль databases"""

from fastapi import FastAPI
import logging
from typing import Optional
from pydantic import BaseModel, Field
import databases
import sqlalchemy
from faker import Faker
from typing import List

app = FastAPI()
fake = Faker()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///hw_db.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()


class TaskIn(BaseModel):
    title: str = Field(..., max_length=16)
    description: str = Field(..., max_length=8)
    done: Optional[bool] = None


class Task(TaskIn):
    id: int


tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("done", sqlalchemy.Boolean),
)


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)


# @app.get("/tasks/{count}")
# async def fill_task_list(count: int):
#     for _ in range(count):
#         query = tasks.insert().values(title=fake.word(), description=fake.text(), done=fake.pybool())
#         await database.execute(query)
#     return {'message': f'{count} fake tasks created'}



@app.get("/tasks/" , response_model=List[Task])
async def read_task():
    query = tasks.select()#.limit(25)
    return await database.fetch_all(query)


@app.get("/tasks/{id_task}", response_model= Task)
async def read_task(id_task: int):
    query = tasks.select().where(tasks.c.id == id_task)
    return await database.fetch_one(query)


@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    return {**task.model_dump(), "id": last_record_id}



@app.put("/tasks/{id_task}", response_model=Task)
async def upd_user(id_task: int, new_tsk: TaskIn):
    query = tasks.update().where(tasks.c.id == id_task).values(new_tsk.model_dump())
    await database.execute(query)
    return {**new_tsk.model_dump(), "id": id_task}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'msg': f'task {task_id} deleted'}


