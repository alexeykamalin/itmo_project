from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING
import re
import bcrypt 
from models.balance import Balance
from models.transaction import Transaction
from models.prediction import Prediction

@dataclass
class User:
    """
    Класс для представления пользователя в системе.
    
    Attributes: comment for git
        id (int): Уникальный идентификатор пользователя
        email (str): Email пользователя
        password (str): Пароль пользователя
        balance (int): Баланс пользователя
        prediction (List['Predition']) список предсказаний
        transaction (List['Transaction']) список транзакций
    """
    id: int
    email: str
    password: str
    balance: Balance
    prediction: List['Prediction'] = field(default_factory=list)
    transaction: List['Transaction'] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._validate_email()
        self._validate_password()
        self._hash_paswd()

    def _validate_email(self) -> None:
        """Проверяет корректность email."""
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(self.email):
            raise ValueError("Invalid email format")
        
    def _hash_paswd(self) -> None:
        """Хешируем пароль"""
        salt = bcrypt.gensalt()
        bytes = self.password.encode()
        hash = bcrypt.hashpw(bytes, salt) 
        self.password = hash

    def _validate_password(self) -> None:
        """Проверяет пароль."""
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        elif self.password.isalnum():
            raise ValueError("Password must have special characters")
        elif self.password.lower() == self.password:
            raise ValueError("Password must have upper case charecters")
        elif self.password.upper() == self.password:
            raise ValueError("Password must have lower case charecters")
        
    def add_prediction(self, prediction: 'Prediction') -> None:
        """Добавляет предсказание в список предсказаний пользователя."""
        self.prediction.append(prediction)

    def add_transaction(self, transaction: 'Transaction') -> None:
        """Добавляет транзакций в список транзакций пользователя."""
        self.transaction.append(transaction)

    def set_balance(self, balance: int) -> None:
        """Изменяет баланс пользователя."""
        self.balance = balance

    def update_password(self, paswd: str) -> None:
        """Изменяет пароль пользователя."""
        self.password = paswd

    def update_email(self, email: str) -> None:
        """Изменяет почту пользователя."""
        self.password = email