from dataclasses import dataclass, field
from typing import List
import re
import bcrypt 

@dataclass
class User:
    """
    Класс для представления пользователя в системе.
    
    Attributes:
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
    prediction: List['Predition'] = field(default_factory=list)
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
        
    def add_prediction(self, prediction: 'Predition') -> None:
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

class Admin(User):
    """
    Класс для представления админов в системе.
    
    Attributes:
        Наследуется от пользователя
    """


@dataclass
class Transaction:
    """
    Класс для представления транзакция.
    
    Attributes:
        id (int): Уникальный идентификатор транзкции
        type (str): Тип транзакции (списание, поступление)
        cost (int): Сумма транзакции
        user (User): Создатель транзакции
        date (str): Дата транзакции
    """
    id: int
    type: str
    cost: int
    user: User
    date: str

    def __post_init__(self) -> None:
        pass

    def get_transaction_by_id(self, id: int) -> None:
        pass

    def get_all_transactions_by_user(self, user: User) -> None:
        pass

    def add_transaction(self, user: User, type: str, cost: int) -> User:
        pass

@dataclass
class Predition:
    """
    Класс для представления предсказаний.
    
    Attributes:
        id (int): Уникальный идентификатор предсказания
        result (str): Результат предсказания (пока не очень понимаю, какой будет результат, поэтому пока строка :) )
        user (User): Создатель предсказания
        date (str): Дата предсказания
    """
    id: int
    result: str
    user: User
    date: str

    def __post_init__(self) -> None:
        pass

    def get_prediction_by_id(self, id: int) -> None:
        pass

    def get_all_predictions_by_user(self, user: User) -> None:
        pass

    def add_prediction(self, user: User) -> None:
        pass

@dataclass
class Balance:
    """
    Класс для работы с балансом пользователя.
    
    Attributes:
        id (int): Уникальный идентификатор баланса
        value (int): значение баланса
        user (User): Юзер с чьим балансом работаем
    """
    id: int
    value: int
    user: User

    def __post_init__(self) -> None:
        pass

    def get_balance(self, user: User) -> None:
        pass

    def set_balance(self, value: int, type: str, user: User) -> None:
        pass

@dataclass
class MLModel:
    """
    Класс ML. Надеюсь модель будет получать картинку и возвращать есть ли на ней машина или нет.
    
    Attributes:
        Нужна помощь не понимаю, что тут  должно быть
    """
    
    def put_image(self) -> None:
        pass
    def get_prediction(self) -> None:
        pass
    def get_config(self) -> None:
        pass
    