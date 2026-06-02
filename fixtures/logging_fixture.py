import logging

import pytest
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@pytest.fixture(scope="session", autouse=True)
def logging_test_pre_post_conditions():
    logging.info("Precondition - Running test....")
    yield
    logging.info("Postcondition - Test finished")
