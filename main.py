# Check if a variable is a Datetime object in Python

from datetime import datetime

today = datetime.today()

print(today)

if isinstance(today, datetime):
    # 👇️ this runs
    print('variable is datetime object')
else:
    print('variable is NOT datetime object')
