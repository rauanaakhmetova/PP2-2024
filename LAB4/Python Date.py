#1 Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta
today = datetime.now()
new_date = today - timedelta(days=5)
print("Today is:", today.strftime("%d-%m-%Y"))
print("5 days ago was:", new_date.strftime("%d-%m-%Y"))

#2Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday was:",  yesterday.strftime("%d-%m-%Y"))
print("Today is:", today.strftime("%d-%m-%Y"))
print("Tommorow wil be:", tomorrow.strftime("%d-%m-%Y"))

#3Write a Python program to drop microseconds from datetime.
from datetime import datetime
datetime = datetime.now()
drop_microseconds = datetime.replace(microsecond=0)
print(datetime)
print(drop_microseconds)


#4Write a Python program to calculate two date difference in seconds.
from datetime import datetime
def date_difference(firstdate, seconddate):
    difference = firstdate - seconddate
    seconds = difference.total_seconds()
    return seconds

firstdate_str = input("YYYY-MM-DD HH:MM:SS")
firstdate = datetime.strptime(firstdate_str, "%Y-%m-%d %H:%M:%S")
seconddate_str = input("YYYY-MM-DD HH:MM:SS")
seconddate = datetime.strptime(seconddate_str, "%Y-%m-%d %H:%M:%S")

result = date_difference(firstdate, seconddate)
print(result)
