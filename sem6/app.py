"""📌 Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:
○ id: int (идентификатор пользователя, генерируется
автоматически)
○ username: str (имя пользователя)
○ email: str (электронная почта пользователя)
○ password: str (пароль пользователя
API должно поддерживать следующие операции:
○ Получение списка всех пользователей: GET /users/
○ Получение информации о конкретном пользователе: GET /users/{user_id}/
○ Создание нового пользователя: POST /users/
○ Обновление информации о пользователе: PUT /users/{user_id}/
○ Удаление пользователя: DELETE /users/{user_id}/"""

from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
import databases
import sqlalchemy
from faker import Faker
from typing import List



DATABASE_URL = "sqlite:///db_sem6.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()



app = FastAPI()

fake = Faker()


class UserIn(BaseModel):
    username: str = Field(..., max_length=32)
    emai: EmailStr = Field(..., max_length=128)
    password: str = Field(..., min_length=6)


class User(UserIn):
    id: int


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(32)),
    sqlalchemy.Column("emai", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(18)),
)


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)


# @app.get("/users/{count}")
# async def create_users(count: int):
#     for _ in range(count):
#         query = users.insert().values(username=fake.name(), emai=fake.email(), password=fake.password())
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


@app.get("/users/", response_model=List[User])
async def get_users():
    query = users.select().limit(25)
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def get_usr_by_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username, emai=user.emai, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.put("/users/{id_user}", response_model=User)
async def upd_user(id_user: int, upd_usr: UserIn):
    query = users.update().where(users.c.id == id_user).values(upd_usr.model_dump())
    await database.execute(query)
    return {**upd_usr.model_dump(), "id": id_user}

@app.delete("/users/{id_user")
async def del_usr(id_user: int):
    query = users.delete().where(users.c.id == id_user)
    await database.execute(query)
    return {'message': 'User deleted'}


