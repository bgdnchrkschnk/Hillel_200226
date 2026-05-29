import pytest


@pytest.mark.authorization
@pytest.mark.api
@pytest.mark.regression
class TestQAutoAPISignUp:

    def test_sign_up_is_successful_with_valid_data(self):
        ...

    def test_sign_up_is_unsuccessful_with_invalid_data(self):
        ...

    def test_sign_up_is_unsuccessful_with_existing_email(self):
        ...

    def test_sign_up_is_unsuccessful_with_existing_username(self):
        ...