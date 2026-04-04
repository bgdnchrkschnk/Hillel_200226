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

class AbstractDBClient(ABC):

    @abstractmethod
    def select(self, query):
        ...

    @abstractmethod
    def mutation(self, query):
        ...

    @abstractmethod
    def health_check(self):
        ...

class SQLClient(AbstractDBClient):

    def select(self, query):
        # sqlite.cursor.execute(query)
        # return sqlite.cursor.fetchall()

    def mutation(self, query):
        # sqlite.cursor.execute(query)

    def health_check(self):
        self.select("SELECT * FROM users")


class PostgresClient(AbstractDBClient):

    def select(self, query):

        # sqlite.cursor.execute(query)
        # return sqlite.cursor.fetchall()

    def mutation(self, query):

        # sqlite.cursor.execute(query)

    def health_check(self):
        self.select("SELECT * FROM users")


class MysqlClient(AbstractDBClient):
    ...

postgres_client = PostgresClient()
postgres_client.select(query="SELECT * FROM users")

mysql_client = MysqlClient()
mysql_client.select(query="SELECT * FROM users")