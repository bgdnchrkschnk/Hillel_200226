import pytest

from tests.base_sausedemo import SauseDemoTestSuite
from utils.date_time import DatetimeUtils


class TestSauseDemoAPI(SauseDemoTestSuite):

    def test_saudemo_api_authorization(self, session):
        DatetimeUtils.date_now()