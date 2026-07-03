from unittest import TestCase

import allure
import pytest

@allure.feature("Sause Demo")
@pytest.mark.regression
@pytest.mark.saudemo
class SauseDemoTestSuite:
    ...