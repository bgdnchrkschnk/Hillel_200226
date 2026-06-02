import logging
from random import choice

import pytest


class TestEmployes:


    @pytest.mark.parametrize("employe_data", [
        {"name": "John", "is_employed": choice([True, False])},
        {"name": "Alex", "is_employed": choice([True, False])},
        {"name": "Michael", "is_employed": choice([True, False])},
    ],ids=["John", "Alex", "Michael"])
    def test_employee_is_employed(self, employe_data):
        logging.info(f"Checking employee: {employe_data}")
        assert employe_data["is_employed"] is True


