from app import User, Transaction, Predition
def main() -> None:
    try:
        user = User(
            id=1,
            email="test@mail.ru",
            password="Secure_password123!",
            balance=0
        )
        
        transaction = Transaction(
            id=1,
            type='add_money',
            cost=100,
            user=user,
            date='30.03.2025'
        )

        predition = Predition(
            id=1,
            result='Пока не понятно',
            user=user,
            date='30.03.2025'
        )
        
        user.add_transaction(transaction)
        user.add_prediction(predition)
        print(f"Created user: {user}")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()