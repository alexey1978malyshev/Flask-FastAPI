"""📌 Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс Movie с полями id, title, description и genre.
📌 Создайте список movies для хранения фильмов.
📌 Создайте маршрут для получения списка фильмов по жанру (метод GET).
📌 Реализуйте валидацию данных запроса и ответа."""


from fastapi import FastAPI
import logging
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Optional[str] = None


movie_1 = Movie(id=1, title="Taxi", description="Lorem ipsum dolor sit amet.", genre="comedy")
movie_2 = Movie(id=2, title="Matrix", description="Lorem ipsum dolor sit amet.", genre="fantastic")
movie_3 = Movie(id=3, title="Fifth element", description="Lorem ipsum dolor sit amet.", genre="fantastic")
movies = [movie_1, movie_2, movie_3]


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "Seminar 5"}


@app.get("/movies")
async def get_movies_genre(genre: str):
    result_lst = []
    for i in range(len(movies)):
        if movies[i].genre == genre:
            result_lst.append(movies[i])
    logger.info(f'Отработал GET запрос для movies - поиск по жанру')
    return result_lst


@app.get("/all_movies")
async def get_all_movies():
    logger.info(f'Отработал GET запрос для movies - получение всего списка')
    return movies



@app.post("/movies/")
async def create_movie(movie: Movie):
    logger.info('Отработал POST запрос создания нового фильма.')
    movies.append(movie)
    return movie


@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, movie: Movie):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            movies[i] = movie
    logger.info(f'Отработал PUT запрос для movie id = {movie}')
    return movie



@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            movies.remove(movies[i])
    logger.info(f'Отработал DELETE запрос для movie_id = {movie_id}.')
    #return {"item_id": item_id}

#
# @app.post("/tasks/")
# async def create_task(task: Task):
#     logger.info('Отработал POST запрос создания новой задачи.')
#     tasks.append(task)
#     return task
#
#
# @app.put("/tasks/{tasks_id}")
# async def update_task(task_id: int, task: Task):
#     for i in range(len(tasks)):
#         if tasks[i].id == task_id:
#             tasks[i] = task
#     logger.info(f'Отработал PUT запрос для task id = {task}')
#     return task
#
#
# @app.delete("/tasks/{tasks_id}")
# async def delete_item(task_id: int):
#     for i in range(len(tasks)):
#         if tasks[i].id == task_id:
#             tasks.remove(tasks[i])
#     logger.info(f'Отработал DELETE запрос для task_id = {task_id}.')
#     #return {"item_id": item_id}