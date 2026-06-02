import logging

import pytest
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@pytest.mark.string_operations
@pytest.mark.smoke
@pytest.mark.regression
class TestStringsSuite:
    """
    Test suite related to strings functionalities (only positive tests)
    """
    def test_upper(self, logging_test_precondition):
        """
        Test verifies that the string is converted to upper case
        """
        input_data: str = "hello"
        print(f"Running check for {input_data}")
        assert input_data.upper() == "HELLO"

    def test_lower(self):
        """
        Test verifies that the string is converted to lower case
        """
        input_data: str = "HELLO"
        assert input_data.lower() != "hello"

@pytest.mark.string_operations
@pytest.mark.regression
class TestStringsNegativeSuite:
    """
    Test suite related to strings functionalities (only negative tests)
    """
    def test_upper_negative(self):
        """
        Test verifies that the error raises when string is converted to upper case with invalid input
        """
        input_data = None
        with pytest.raises(AttributeError) as e:
            input_data.upper()