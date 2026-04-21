import os

from dotenv import load_dotenv
load_dotenv()


def connect_to_db(username, password, host, port, database):
    print("Connecting to DB with username: ", username, "password: ", password, "host: ", host, "port: ", port, "database: ", database)

connect_to_db(username=os.getenv("DEV_DB_USER"),
              password=os.getenv("DEV_DB_PASSWORD"),
              host=os.getenv("DEV_DB_HOST"),
              port=os.getenv("DEV_DB_PORT"),
              database=os.getenv("DEV_DB_NAME"))

min(1,2)