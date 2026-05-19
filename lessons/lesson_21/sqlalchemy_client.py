import logging
import os
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from lessons.lesson_21.data_provider.user_data_provider import get_user
from lessons.lesson_21.declarative_base import Base
from lessons.lesson_21.table_models.users_table import User
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
load_dotenv()


class SQLAlchemyClient:

    def __init__(self):
        self.db_url = os.getenv("POSTGRES_DB_URL")
        self.__engine: Engine = create_engine(self.db_url)
        self.__session = self.__create_session()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine

    def __create_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def create_table(self, table_model):
        table_model.metadata.create_all(self.engine)

    def create_all_tables(self):
        Base.metadata.create_all(self.engine)

    def close_connection(self):
        self.session.close()
        # self.engine.dispose()


if __name__ == "__main__":
    sqlalchemy_client = SQLAlchemyClient()
    sqlalchemy_client.create_table(table_model=User)

    # --------------------- insert new user

    # new_user: User = get_user()
    # logging.info(new_user.__dict__)
    # sqlalchemy_client.session.add(new_user)
    # sqlalchemy_client.session.commit()

    # --------------------- insert 10 new users
    # new_10_users: list[User] = [get_user() for i in range(10)]
    # ---------
    # for user in new_10_users:
    #     sqlalchemy_client.session.add(user)
    # sqlalchemy_client.session.commit()

    sqlalchemy_client.session.add_all(new_10_users)
    sqlalchemy_client.session.commit()


    # ---------------------- Updating a record
    # user_to_update = sqlalchemy_client.session.query(User).filter_by(name="James Graves").first() # filter_by -> WHERE SELECT * FROM users WHERE id=
    # user_to_update.name = "WASTED"
    # sqlalchemy_client.session.commit()


    # ---------------------- Updating multiple records
    # users_to_update = sqlalchemy_client.session.query(User).filter(User.age < 18).all()
    # for user in users_to_update:
    #     user.name += " [NOT ADULT]"
    #     # user.name = user.name + " [NOT ADULT]"
    # sqlalchemy_client.session.commit()
    #
    #
    # incorrect_users = sqlalchemy_client.session.query(User).filter(User.age > 69).all()
    # for user in incorrect_users:
    #     sqlalchemy_client.session.delete(user)
    # sqlalchemy_client.session.commit()







