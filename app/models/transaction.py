from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

class TransactionBase(SQLModel):
    type: str
    cost: int

class Transaction(TransactionBase, table=True):
    """
    Класс для представления транзакция.
    
    Attributes:
        id (int): Уникальный идентификатор транзкции
        type (str): Тип транзакции (списание, поступление)
        cost (int): Сумма транзакции
        user (User): Создатель транзакции
        date (str): Дата транзакции
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    creator: Optional['User']= Relationship(
        back_populates="transactions"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    def __str__(self) -> str:
        result = (f"Id: {self.id}. Type: {self.type}. Creator: {self.user.email}. Cost: {self.cost}")
        return result
    
class TransactionCreate(TransactionBase):
    """
    
    """
    pass

class TransactionUpdate(TransactionBase):
    type: str = None
    cost: int = None

    class Config:
        """Model configuration"""
        validate_assignment = True