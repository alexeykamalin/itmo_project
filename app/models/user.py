from sqlmodel import SQLModel, Field, Relationship, Column, func, DateTime
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
import re

class User(SQLModel, table=True):
    """
    Класс для представления пользователя в системе.
    
    Attributes:
        id (int): Primary key
        email (str): users email
        password (str): paswd hash
        created_at (datetime): creation time
        balanse (Balanse): user balanse
        predictions (List[Prediction]): list of user predictions
        transactions (List[Transaction]): list of user transactions
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, min_length=5, max_length=255)
    password: str = Field(min_length=8)
    name: str = Field(min_length=2)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    transactions: Optional[List["Transaction"]] = Relationship(
        back_populates="creator",
    )
    predictions: Optional[List["Prediction"]] = Relationship(
        back_populates="creator",
    )
    balance: Optional["Balance"] = Relationship(
        back_populates="creator",
    )

    def __str__(self) -> str:
        return f"Id: {self.id}. Email: {self.email}. Tranactions: {self.transactions}. Balance: {self.balance}"
    
    def validate_email(self) -> bool:
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not pattern.match(self.email):
            raise ValueError("Invalid email format")
        return True

    @property
    def tranaction_count(self) -> int:
        """Number of events associated with user"""
        return len(self.tranaction)

    class Config:
        """Model configuration"""
        validate_assignment = True
        arbitrary_types_allowed = True