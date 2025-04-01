from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User

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