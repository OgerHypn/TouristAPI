from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from dataclasses import dataclass


class UserInfo(BaseModel):
    email: Optional[str] = Field(default=None, description='Эл. почта пользователя', example='ggrtyy@mail.ru')
    fam: str = Field(description='Фамилия пользователя', example='Иванов')
    name: str = Field(description='Имя пользователя', example='Иван')
    otc: Optional[str] = Field(default=None, description='Отчество пользователя', example='Иванович')
    phone: str = Field(description='Телефон пользователя', example='+7 999 99 99')


class CoordsInfo(BaseModel):
    latitude: float = Field(description='Широта', example=54.4656)
    longitude: float = Field(description='пользователя', example=9.4577)
    height: int = Field(description='пользователя', example=1500)


class LevelInfo(BaseModel):
    winter: str = Field(description='Категория трудности. Зима.', example='')
    summer: str = Field(description='Категория трудности. Лето.', example='A1')
    autumn: str = Field(description='Категория трудности. Осень', example='')
    spring: str = Field(description='Категория трудности. Весна.', example='')


class ImageInfo(BaseModel):
    data: str = Field(description='Фото в Base64', example='data:image/jpg;base64,/9j/4AA..')
    title: str = Field(description='Название фото', example='Альпы')


class BodyInfo(BaseModel):
    beauty_title: str = Field(description='Сокращенное название', example='пер. ')
    title: str = Field(description='Название', example='Пхия')
    other_titles: str = Field(description='Народное название', example='Триев')
    connect: str = Field(description='Что соединяет', example='Текстовое поле')
    add_time: datetime = Field(description='Время добавления', example=datetime.utcnow().isoformat())
    user: UserInfo = Field(
        description='Пользователь',
        example={
            'email': 'ggrtyy@mail.ru',
            'fam': 'Иванов',
            'name': 'Иван',
            'otc': 'Иванович',
            'phone': '+7 999 99 99'
        }
    )
    coords: CoordsInfo = Field(description='пользователя', example='havet')
    level: LevelInfo = Field(description='пользователя', example='havet')
    images: List[ImageInfo] = Field(description='пользователя', example='havet')


@dataclass
class User:
    phone: str
    fam: str
    name: str
    id: Optional[int] = None
    email: Optional[str] = None
    otc: Optional[str] = None


@dataclass
class Coords:
    latitude: float
    longitude: float
    height: int
    id: Optional[int] = None


@dataclass
class Level:
    winter: str
    summer: str
    autumn: str
    spring: str
    id: Optional[int] = None


@dataclass
class Image:
    image: str
    title: str
    data_id: int
    id: Optional[int] = None


@dataclass
class Data:
    beauty_title: str
    title: str
    other_titles: str
    connect: str
    add_time: datetime
    user_id: int
    coords_id: int
    level_id: int
    id: Optional[int] = None


