from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

class PredictionBase(SQLModel):
    """
    """
    result: str

class Prediction(PredictionBase, table=True):
    """
    Класс для представления предсказаний.
    
    Attributes:
        id (int): Уникальный идентификатор предсказания
        result (str): Результат предсказания (пока не очень понимаю, какой будет результат, поэтому пока строка :) )
        user (User): Создатель предсказания
        date (str): Дата предсказания
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    creator: Optional['User']= Relationship(
        back_populates="predictions"
    )

    def __str__(self) -> str:
        result = (f"Id: {self.id}. Result: {self.result}. Creator: {self.user.email}")
        return result
    
class PredictionCreate(PredictionBase):
    """
    
    """
    pass

class PredictionUpdate(PredictionBase):
    result: str = None

    class Config:
        """Model configuration"""
        validate_assignment = True