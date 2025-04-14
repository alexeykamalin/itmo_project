from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, func, DateTime
from typing import Optional, List, TYPE_CHECKING

class Prediction(SQLModel, table=True):
    """
    Класс для представления предсказаний.
    
    Attributes:
        id (int): Уникальный идентификатор предсказания
        result (str): Результат предсказания (пока не очень понимаю, какой будет результат, поэтому пока строка :) )
        user (User): Создатель предсказания
        date (str): Дата предсказания
    """
    result: str
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    creator: Optional['User']= Relationship(
        back_populates="predictions"
    )

    def __str__(self) -> str:
        result = (f"Id: {self.id}. Result: {self.result}. Creator: {self.user.email}")
        return result