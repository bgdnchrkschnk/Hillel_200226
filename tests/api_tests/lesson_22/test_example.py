import sys
from datetime import datetime

import pytest


def get_os() -> str:
    """
    win - win32
    mac - darwin
    linux - linux
    """
    return sys.platform

@pytest.mark.regression
class TestExample:

    @pytest.mark.skipif(datetime.now().day == 27, reason="Test is not working on 26th")
    def test_27_true(self):
        assert True

    @pytest.mark.skipif(get_os() == "darwin", reason="Test is not working on Win")
    def test_only_macos(self):
        assert True