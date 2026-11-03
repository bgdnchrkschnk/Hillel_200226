from abc import ABC, abstractmethod


# Клас називається абстрактним якщо в нього є хоча б 1 абстрактний метод

class Animal(ABC):

    @abstractmethod # зробити обовязковим у підкласах
    def move(self):
        ...

    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    def move(self):
        print("Dog is moving")

    def sleep(self):
        print("Dog is sleeping")

class Cat(Animal):
    def move(self):
        print("Cat is moving")

class Bird(Animal):
    def move(self):
        print("Bird is moving")

dog = Dog()
cat = Cat()
bird = Bird()

dog.move()
cat.move()
bird.move()

dog.sleep()
cat.sleep()
bird.sleep()


#################################
import sqlite3
import psycopg2  # type: ignore
from abc import ABC, abstractmethod
from decimal import Decimal


# 1. Абстрактний клас
class AbstractAQADBClient(ABC):

    @abstractmethod
    def seed_user(self, username: str, initial_balance: Decimal) -> str:
        """SETUP (Arrange): Створює тестового користувача та повертає його user_id."""
        pass

    @abstractmethod
    def assert_user_balance(self, user_id: str, expected_balance: Decimal) -> bool:
        """VALIDATION (Assert): Перевіряє остаточний баланс користувача в БД."""
        pass

    @abstractmethod
    def reset_database(self) -> None:
        """CLEANUP (Teardown): Повністю очищує тестові таблиці між тестами."""
        pass


# 2. SQLite Реалізація (Local / Fast CI)
class SQLiteAQADBClient(AbstractAQADBClient):

    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)

    def seed_user(self, username: str, initial_balance: Decimal) -> str:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, balance) VALUES (?, ?)",
            (username, float(initial_balance))
        )
        self.conn.commit()
        return str(cursor.lastrowid)

    def assert_user_balance(self, user_id: str, expected_balance: Decimal) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        actual_balance = Decimal(str(row[0])) if row else Decimal("0")
        return actual_balance == expected_balance

    def reset_database(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users;")
        self.conn.commit()


# 3. Postgres Реалізація (Integration CI / Staging)
class PostgresAQADBClient(AbstractAQADBClient):

    def __init__(self, dsn: str):
        self.conn = psycopg2.connect(dsn)

    def seed_user(self, username: str, initial_balance: Decimal) -> str:
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, balance) VALUES (%s, %s) RETURNING id;",
                (username, initial_balance)
            )
            user_id = cursor.fetchone()[0]
            self.conn.commit()
            return str(user_id)

    def assert_user_balance(self, user_id: str, expected_balance: Decimal) -> bool:
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT balance FROM users WHERE id = %s;", (user_id,))
            row = cursor.fetchone()
            actual_balance = Decimal(str(row[0])) if row else Decimal("0")
            return actual_balance == expected_balance

    def reset_database(self) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE users CASCADE;")
            self.conn.commit()