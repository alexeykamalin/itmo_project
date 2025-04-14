from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, func, DateTime
from typing import Optional, List, TYPE_CHECKING

class Balance(SQLModel, table=True):
    """
    Класс для работы с балансом пользователя.
    
    Attributes:
        id (int): Уникальный идентификатор баланса
        value (int): значение баланса
        user (User): Юзер с чьим балансом работаем
    """
    value: int = Field(default=0)
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    creator: Optional['User']= Relationship(
        back_populates="balance"
    )