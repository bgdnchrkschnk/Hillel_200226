import logging
import os
from dotenv import load_dotenv
import psycopg2
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


load_dotenv()


class DBClient:

    def __init__(self):
        self.username = os.getenv("DEV_DB_USER")
        self.password = os.getenv("DEV_DB_PASSWORD")
        self.host = os.getenv("DEV_DB_HOST")
        self.port = os.getenv("DEV_DB_PORT")
        self.db_name = os.getenv("DEV_DB_NAME")
        self.__connect()

    @property
    def cursor(self):
        return self.__cursor

    def __connect(self):
        try:
            self.__connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.db_name,
                user=self.username,
                password=self.password)
            self.__connection.autocommit = True
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            logging.error(f"Connection error: {e}\nCredentials: {self.username} {self.password}")
            raise e
        else:
            logging.info("Connection successful")

    def select(self, query: str) -> list[dict]:
        logging.info(f"Executing query: {query}")
        self.cursor.execute(query) # execute - query
        result = self.cursor.fetchall()
        return result

    def mutation(self, query: str):
        logging.info(f"Executing query: {query}")
        self.cursor.execute(query) # execute - query

    def close(self):
        self.__cursor.close()
        self.__connection.close()

    def clear_test_data_for_today(self):
        self.mutation("DELETE FROM users WHERE created_at = NOW()")


if __name__ == "__main__":
    db_client = DBClient()

    db_client.mutation("INSERT INTO users (name) VALUES ('python_user')")
    selected_users = db_client.select("SELECT * FROM users")
    print(selected_users)
    ...





# db_client = DBClient()
# db_client.__cursor
# db_client.cursor
# db_client.cursor = "dghe"

