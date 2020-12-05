
from dateutil.parser import parse
from datetime import datetime


date = 'Fri May 10 00:44:04 +0000 2019'
dt = parse(date)

print(dt)
print(type(dt))

timestamp = datetime.timestamp(dt)

print(timestamp)
