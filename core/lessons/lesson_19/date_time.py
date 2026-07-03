import time
from time import sleep
from datetime import datetime


def hello(delay=0):
    sleep(delay)
    print("Hello")



date_time_now: datetime = datetime.now()
print(type(date_time_now), dir(date_time_now), date_time_now, sep="\n")


# Тільки дата
date_now = date_time_now.date()
print(date_now)

# Тільки час
time_now = date_time_now.time()
print(time_now)


year_now: int = date_time_now.year
month_now: int = date_time_now.month
day_now: int = date_time_now.day
hour_now: int = date_time_now.hour
minute_now: int = date_time_now.minute
second_now: int = date_time_now.second
microsecond_now: int = date_time_now.microsecond


print(year_now, month_now, day_now, hour_now, minute_now, second_now, microsecond_now)


datetime_war_start: datetime = datetime(year=2022, month=2, day=24, hour=4, minute=20)

war_year_start: int = datetime_war_start.year
war_month_start: int = datetime_war_start.month
war_day_start: int = datetime_war_start.day
war_hour_start: int = datetime_war_start.hour
war_minute_start: int = datetime_war_start.minute
war_second_start: int = datetime_war_start.second
war_microsecond_start: int = datetime_war_start.microsecond


date_war_start = datetime_war_start.date()
time_war_start = datetime_war_start.time()


print(type(date_war_start), date_war_start)
print(type(time_war_start),time_war_start)

# def is_leap_year(date_time: datetime) -> None:
#     if date_time.year % 4 == 0:
#         print("Leap year")
#     else:
#         print("Not leap year")
#
#
# is_leap_year(datetime_war_start)

# UNIX TIME

unix_time_from_datetime_object = datetime_war_start.timestamp() #UNIX time

UNIX_TIME = str(time.time()) # generation of unix time
datetime.now().timestamp()
