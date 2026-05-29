import pytest


@pytest.mark.authorization
@pytest.mark.e2e
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
class TestAuthQAutoAPI:

    def test_sign_up_and_sign_in_and_sign_out(self):
        ...


