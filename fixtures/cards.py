import pytest


@pytest.fixture
def premium_card() -> dict:
    return {"card_type": "Premium", "card_number": 123456789}

@pytest.fixture()
def basic_card() -> dict:
    return {"card_type": "Basic", "card_number": 123456759}

@pytest.fixture
def platinum_card() -> dict:
    return {"card_type": "Platinum", "card_number": 134456799}