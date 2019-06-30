#Test script to work out billion second birthday

import datetime as dt

print("What is your date of birth?")
Day = (int(input("Day (format: DD): ")))
Month = (int(input("Month (format: MM): ")))
Year = (int(input("Year (format: YYYY): ")))

print("\nWhat is your time of birth?")
Hour = (int(input("Hour (format HH (24h)): ")))
Minute = (int(input("Minute (format MM): ")))

date = dt.datetime(Year,Month,Day,Hour,Minute)
timedelta = dt.timedelta(seconds=1000000000)

newdate = date + timedelta

if newdate.hour < 12:
    clock = 'am'
else:
    clock = 'pm'

print("\nYour Billion Second Birthday is: ", newdate.day,"-",newdate.month,"-",newdate.year,", at ",newdate.hour,":",newdate.minute,clock)