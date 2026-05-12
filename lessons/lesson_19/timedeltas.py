from datetime import datetime, timedelta


now: datetime = datetime.now()

delta_4_weeks: timedelta = timedelta(weeks=4)

now_plus_4_weeks: datetime = now - delta_4_weeks

print(now_plus_4_weeks, type(now_plus_4_weeks))



# --------------------------------------------- timedelta between two datetime objects

datetime_war_start: datetime = datetime(year=2022, month=2, day=24, hour=4, minute=20)
datetime_war_end: datetime = datetime(year=2026, month=6, day=5, hour=4, minute=35, second=12, microsecond=123456)


def get_timedelta(d1: datetime, d2: datetime) -> timedelta:
    return abs(d2-d1)


war_time: timedelta = get_timedelta(datetime_war_end, datetime_war_start)

print(type(war_time), war_time)
