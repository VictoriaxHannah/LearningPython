#Test script to work out billion second birthday, taking into account daylight saving.

# leap seconds do not need accounting for. There have only been 27 leap seconds added,
# and since DOB is added as hours and minutes, the leap seconds will not change the day
# of Billion Second Birthday.
 
import datetime as dt
import pytz

local = pytz.timezone('Europe/London')
utc = pytz.utc

print("What is your date of birth?")
Day = (int(input("Day (format: DD): ")))
Month = (int(input("Month (format: MM): ")))
Year = (int(input("Year (format: YYYY): ")))

print("\nWhat is your time of birth?")
Hour = (int(input("Hour (format HH (24h)): ")))
Minute = (int(input("Minute (format MM): ")))

date = dt.datetime(Year,Month,Day,Hour,Minute)
utcbirth = date.astimezone(utc)

timedelta = dt.timedelta(seconds=1000000000)

newutcdate = utcbirth + timedelta
locdate = newutcdate.astimezone(local)

if locdate.hour < 12:
    clock = 'am'
else:
    clock = 'pm'

print("\nYour Billion Second Birthday is: ", locdate.day,"-",locdate.month,"-",locdate.year,", at ",locdate.hour,":",locdate.minute,clock)