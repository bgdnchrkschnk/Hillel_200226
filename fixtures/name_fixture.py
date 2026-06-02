from random import choice

import pytest


@pytest.fixture(params=["John", "Alex", "Michael"])
def get_person(request):
    name = request.param
    employee_dict = {"name": name, "is_employed": choice([True, False])}
    yield employee_dict