from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones



all_timezones = available_timezones()
all_eu_timezones = [timezone for timezone in all_timezones if timezone.startswith("Europe/")]


datetime_now_kyiv = datetime.now(tz=ZoneInfo("Europe/Kyiv"))
date_now_paris = datetime.now(tz=ZoneInfo("Europe/Paris"))

print("Date Kyiv and Paris the same:", datetime_now_kyiv.date() == date_now_paris.date())
print("Time Kyiv and Paris the same:", datetime_now_kyiv.time() == date_now_paris.time())
print("Timezones are same:", datetime_now_kyiv.tzinfo == date_now_paris.tzinfo)


# astimezone() - converting datetime object to another timezone
datetime_war_start: datetime = datetime(year=2022, month=2, day=24, hour=4, minute=20, tzinfo=ZoneInfo("Europe/Kyiv"))

datetime_war_start_la: datetime = datetime_war_start.astimezone(ZoneInfo("America/Los_Angeles"))
datetime_war_start_japan: datetime = datetime_war_start.astimezone(ZoneInfo("Asia/Tokyo"))
#
# print(datetime_war_start_japan)
#
#
# print("Date the same:", datetime_war_start.date() == datetime_war_start_japan.date())
# print("Time the same:", datetime_war_start.time() == datetime_war_start_japan.time())
# print("Timezones are same:", datetime_war_start.tzinfo == datetime_war_start_japan.tzinfo)


# replace() - replacing timezone of datetime object
datetime_war_start: datetime = datetime(year=2022, month=2, day=24, hour=4, minute=20, tzinfo=ZoneInfo("Europe/Kyiv"))

datetime_war_start_tokyo = datetime_war_start.replace(tzinfo=ZoneInfo("Asia/Tokyo"))

print(datetime_war_start_tokyo.date() == datetime_war_start.date())
print(datetime_war_start_tokyo.time() == datetime_war_start.time())


#
datetime_war_start_utc = datetime_war_start.astimezone(ZoneInfo("UTC"))








