import logging

import pytest
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@pytest.fixture(scope="session")
def logging_test_pre_post_conditions():
    logging.info("INNER CONFTEST Precondition - Running test....")
    yield
    logging.info("INNER CONFTEST Postcondition - Test finished")
