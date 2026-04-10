# import unittest # not best practice
from unittest import TestCase, main
from lessons.lesson_12.register_service import register_user, RegistrationServiceError


class TestRegistrationService(TestCase):
    """
    Test class for checking registration service
    """
    def test_registration_login_is_successful(self):
        """
        Test with valid data - login is successful
        """
        test_username = "test_user"
        test_password = "gugfHEWhf"
        test_email = "test_email@test.com"
        test_phone = "123456789"
        actual_response: dict = register_user(test_username, test_password, test_email, test_phone)
        assert actual_response.get("status_code") == 200, f"It was expected 200 status_code, but got {actual_response.get('status_code')}"
        assert actual_response.get("success") == True, f"It was expected True success, but got {actual_response.get('success')}"
        assert actual_response.get("user") == {"username": test_username, "email": test_email, "phone": test_phone}, f"User data is not correct in response"


class TestRegistrationServiceNegatives(TestCase):
    """
    Test class for checking registration service (negative cases)
    """
    def test_registration_with_invalid_email_1(self):
        test_username = "test_user"
        test_password = "gugfHEWhf"
        test_email = "test_email@@test.com"
        test_phone = "123456789"
        actual_response: dict = register_user(test_username, test_password, test_email, test_phone)
        assert actual_response.get("status_code") != 200
        assert actual_response.get("success") == False
        assert "error" in actual_response.keys()

    def test_registration_with_invalid_email_2(self):
        test_username = "test_user"
        test_password = "gugfHEWhf"
        test_email = "test_emailtest.com"
        test_phone = "123456789"
        actual_response: dict = register_user(test_username, test_password, test_email, test_phone)
        assert actual_response.get("status_code") != 200
        assert actual_response.get("success") == False
        assert "error" in actual_response.keys()

    def test_registration_with_existing_user(self):
        """
        Testing service on raised exception
        """
        test_username = "registered_user"
        test_password = "jekfHEFIAa"
        test_email = "registered_user@test.com"
        test_phone = "123456789"
        with self.assertRaises(RegistrationServiceError):
            register_user(test_username, test_password, test_email, test_phone)

# assert <condition> -> AssertionError
if __name__ == '__main__':
    main(verbosity=2)