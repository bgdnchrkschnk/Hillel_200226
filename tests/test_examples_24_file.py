
"""
fixture scopes:
session - once per session
module - once per test file
class - once per test class
function - once per test function
"""
import pytest
import logging
from faker import Faker
fake = Faker()


# @pytest.fixture # scope=function
# def logging_test_precondition():
#     logging.info("Precondition - Running test....")
#     yield # test execution
#
# @pytest.fixture
# def logging_test_postcondition():
#     yield
#     logging.info("Postcondition - Test finished")



class TestExamples24:

    def test_assert_true(self):
        assert True

    def test_string_is_upper(self):
        test_string = "hello"
        assert "hello".upper() == "HELLO"

    def test_multiplication(self):
        assert 7 * 7 == 49

    def test_is_empty(self):
        assert not [] # bool([])


class TestExamples24Second:

    def test_assert_true(self):
        assert True

    def test_string_is_upper(self):
        test_string = "hello"
        assert "hello".upper() == "HELLO"

    @pytest.mark.parametrize("a, b, expected_result", [
        (2, 7, 14),
        (3, 9, 27),
        (5, 10, 50)
    ], ids=["2x7", "3x9", "5x10"])
    def test_multiplication(self, a, b, expected_result):
        assert a * b == expected_result

    def test_is_empty(self):
        assert not [] # bool([])

    def test_test_order_is_valid(self, random_test_order):
        assert "TEST_ORDER" in random_test_order
