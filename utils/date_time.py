from datetime import datetime


class DatetimeUtils:

    @staticmethod
    def date_now():
        return datetime.now().date()

    @staticmethod
    def time_now():
        return datetime.now().time()
