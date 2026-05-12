from datetime import datetime
from zoneinfo import ZoneInfo




transaction_time = datetime(year=2026, month=5, day=12, hour=21, minute=20, tzinfo=ZoneInfo("Asia/Tbilisi"))

now = datetime.now(tz=ZoneInfo("UTC"))

def process_transaction(transaction: datetime):
    transaction_utc = transaction.astimezone(ZoneInfo("UTC"))
    print("Transaction UTC time: ", transaction_utc)
    if transaction_utc.date() == now.date():
        print("Processing transaction...", "Date of payout", now.date())
    else:
        print("Skipping transaction...")


process_transaction(transaction_time)