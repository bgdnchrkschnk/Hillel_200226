import unittest

from is_adult import is_adult
from lessons.lesson_13.custom_logger_full import custom_logger_full


class TestIsAdult(unittest.TestCase):

    def test_is_adult_logging(self):
        with self.assertLogs(logger=custom_logger_full, level='INFO'):
            is_adult()


            with open("log.log", "r") as f:
                data = f.read()[-1]