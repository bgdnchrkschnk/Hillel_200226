from psycopg2 import connect

class TestDocker:
    # def test_db_conn(self):
    #     conn = connect(
    #         dbname="test_db",
    #         user="test_user",
    #         password="test_password",
    #         host="localhost",
    #         port="5432"
    #     )
    #     assert conn


    def test_db_conn_cl(self):
        conn = connect(
            dbname="test_db",
            user="test_user",
            password="test_password",
            host="db",
            port="5433"
        )
        assert conn
