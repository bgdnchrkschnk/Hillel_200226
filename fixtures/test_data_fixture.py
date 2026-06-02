import time

import pytest


@pytest.fixture(autouse=True)
def random_test_order():
    yield "TEST_ORDER_"+str(time.time())