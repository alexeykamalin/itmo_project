from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User

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