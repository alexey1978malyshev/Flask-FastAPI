"""📌 Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс User с полями id, name, email и password.
📌 Создайте список users для хранения пользователей.
📌 Создайте маршрут для добавления нового пользователя (метод POST).
📌 Создайте маршрут для обновления информации о пользователе (метод PUT).
📌 Создайте маршрут для удаления информации о пользователе (метод DELETE).
📌 Реализуйте валидацию данных запроса и ответа."""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import logging
from typing import Optional
from pydantic import BaseModel
from .forms import RegisterForm
from flask import url_for


app = FastAPI()
templates = Jinja2Templates(directory="Flask-FastAPI/sem5/HW/templates")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


user_1 = User(id=1, name='Иванов И.И.', email='asd@asd.asd', password='asdasdasd')
user_2 = User(id=2, name='Петров П.П.', email='qwe@qwe.qwe', password='qweqweqwe')
user_3 = User(id=3, name='Сидоров С.С.', email='zxc@zxc.zxc', password='zxczxczxc')
users = [user_1, user_2, user_3]


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "HW sem5"}


@app.get("/users/", response_class=HTMLResponse)
async def all_users(request: Request):
    logger.info('Отработал GET запрос вывода списка пользователей.')
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.post("/add_user/", response_class=HTMLResponse)
async def add_user(request: Request, user: User):
    form = RegisterForm()
    user.id = len(users)
    user.name = form.name.data
    user.email = form.email.data
    user.password = form.password.data
    users.append(user)
    logger.info('Отработал POST запрос создания нового пользователя.')
    return templates.TemplateResponse("users.html", {"request": request, "form": form})


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = user
            logger.info(f'Отработал PUT запрос для user_id  = {user.name}')
            return user
    return HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            users.remove(users[i])
    logger.info(f'Отработал DELETE запрос для user_id = {user_id}.')
