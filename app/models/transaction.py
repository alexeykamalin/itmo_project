from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, func, DateTime
from typing import Optional, List, TYPE_CHECKING

class Transaction(SQLModel, table=True):
    """
    Класс для представления транзакция.
    
    Attributes:
        id (int): Уникальный идентификатор транзкции
        type (str): Тип транзакции (списание, поступление)
        cost (int): Сумма транзакции
        user (User): Создатель транзакции
        date (str): Дата транзакции
    """
    type: str
    cost: int
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    creator: Optional['User']= Relationship(
        back_populates="transactions"
    )
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    
    def __str__(self) -> str:
        result = (f"Id: {self.id}. Type: {self.type}. Creator: {self.user.email}. Cost: {self.cost}")
        return result