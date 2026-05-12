from datetime import datetime



# -------------------------------- from datetime string to datetime object

datetime_string_1 = "2024-11-30 17:55:59"
datetime_string_2 = "24-17-03T5:55:30 PM"
datetime_string_3 = "20-02-20 8:55:30.255 -0200"


datetime_1: datetime = datetime.strptime(datetime_string_1, "%Y-%m-%d %H:%M:%S")

year: int = datetime_1.year
month: int = datetime_1.month
day: int = datetime_1.day
hour: int = datetime_1.hour
minute: int = datetime_1.minute
second: int = datetime_1.second
microsecond: int = datetime_1.microsecond
tz_info = datetime_1.tzinfo

datetime_2: datetime = datetime.strptime(datetime_string_2, "%y-%d-%mT%H:%M:%S %p")

year_2: int = datetime_2.year
month_2: int = datetime_2.month
day_2: int = datetime_2.day
hour_2: int = datetime_2.hour
minute_2: int = datetime_2.minute
second_2: int = datetime_2.second
microsecond_2: int = datetime_2.microsecond
tz_info_2 = datetime_2.tzinfo

datetime_3: datetime = datetime.strptime(datetime_string_3, "%y-%m-%d %H:%M:%S.%f %z")

year_3: int = datetime_3.year
month_3: int = datetime_3.month
day_3: int = datetime_3.day
hour_3: int = datetime_3.hour
minute_3: int = datetime_3.minute
second_3: int = datetime_3.second
microsecond_3: int = datetime_3.microsecond
tz_info_3 = datetime_3.tzinfo


print(datetime_3.tzinfo)


# --------------------------------------------- from datetime object to datetime string


datetime_war_end = datetime(year=2026, month=6, day=5, hour=4, minute=35, second=12, microsecond=123456)

war_end_string_datetime: str = datetime_war_end.strftime("%y-%m-%d %H:%M:%S.%f %z")
print(war_end_string_datetime)
