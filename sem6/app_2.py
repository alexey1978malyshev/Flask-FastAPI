"""Создать веб-приложение на FastAPI, которое будет предоставлять API для
работы с базой данных пользователей. Пользователь должен иметь
следующие поля:
○ ID (автоматически генерируется при создании пользователя)
○ Имя (строка, не менее 2 символов)
○ Фамилия (строка, не менее 2 символов)
○ Дата рождения (строка в формате "YYYY-MM-DD")
○ Email (строка, валидный email)
○ Адрес (строка, не менее 5 символов)
API должен поддерживать следующие операции:
○ Добавление пользователя в базу данных
○ Получение списка всех пользователей в базе данных
○ Получение пользователя по ID
○ Обновление пользователя по ID
○ Удаление пользователя по ID
📌 Приложение должно использовать базу данных SQLite3 для хранения
пользователей."""


from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
import databases
import sqlalchemy
from faker import Faker
from typing import List
from datetime import date



DATABASE_URL = "sqlite:///db2_sem6.db"

database = databases.Database(DATABASE_URL)



metadata = sqlalchemy.MetaData()



app = FastAPI()

fake = Faker()


class UserIn(BaseModel):
    username: str = Field(..., max_length=32, min_length=2)
    birth_date: date
    email: EmailStr = Field(..., max_length=128)
    address: str = Field(..., min_length=6)


class User(UserIn):
    id: int


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(32)),
    sqlalchemy.Column("birth_date", sqlalchemy.Date()),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("address", sqlalchemy.String(20)),
)


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)


# @app.get("/users/{count}")
# async def create_users(count: int):
#     for _ in range(count):
#         query = users.insert().values(username=fake.name(), birth_date=fake.date_of_birth(), email=fake.email(),
#                                       address=fake.address())
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
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.put("/users/{id_user}", response_model=User)
async def upd_user(id_user: int, upd_usr: UserIn):
    query = users.update().where(users.c.id == id_user).values(upd_usr.model_dump())
    await database.execute(query)
    return {**upd_usr.model_dump(), "id": id_user}

@app.delete("/users/{id_user}")
async def del_usr(id_user: int):
    query = users.delete().where(users.c.id == id_user)
    await database.execute(query)
    return {'message': 'User deleted'}


