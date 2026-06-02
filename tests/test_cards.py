from random import choice


class TestCards:



    def test_basic_card(self):
        # basic_card = {"card_type": "Basic", "card_number": 123456759}
        # response = api_client.make_payment(basic_card, amount=100)
        # db_client.find_payment_is_successful(response['payment_id'])
        status = choice(["success", "failed"])
        assert status == "success"


    def test_basic_card_merchant_premium(self):
        assert basic_card
        ...



    def test_basic_card_merchant_regular(self, basic_card):
        ...
