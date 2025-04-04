from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User
    
@dataclass
class Admin(User):
    """
    Класс для представления админов в системе.
    
    Attributes:
        Наследуется от пользователя
        users: List['User'] = field(default_factory=list)
    """
    def get_all_users(self) -> None:
        """Получение списка всех пользователей."""
        self.users.append(User)