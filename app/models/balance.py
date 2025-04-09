from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

class BalanceBase(SQLModel):
    value: int = Field(default=0)

class Balance(BalanceBase, table=True):
    """
    Класс для работы с балансом пользователя.
    
    Attributes:
        id (int): Уникальный идентификатор баланса
        value (int): значение баланса
        user (User): Юзер с чьим балансом работаем
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.time)
    creator: Optional['User']= Relationship(
        back_populates="balance"
    )
    
class BalanceCreate(BalanceBase):
    """
    
    """
    pass

class BalanceUpdate(BalanceBase):
    result: str = None

    class Config:
        """Model configuration"""
        validate_assignment = True