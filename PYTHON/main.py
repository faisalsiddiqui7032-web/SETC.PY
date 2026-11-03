## Q.1  ## SECTION A:  DATE & TIME MATH, RANDOM, UUID, TIME.

from datetime import datetime, timedelta

# 1. Leap Year Function
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


years = [1700, 2016, 2026, 2200, 2032]

for year in years:
    print(year, is_leap_year(year))


# 2. Day of Week Function
def day_of_week(text):
    date = datetime.strptime(text, "%Y-%m-%d")
    return date.strftime("%A")


dates = ['2026-05-01', '2026-10-02', '2027-03-14']

for date in dates:
    print(date, day_of_week(date))


# 3. Number of Days Between Two Dates
date1 = datetime(2026, 3, 10)
date2 = datetime(2026, 9, 20)

difference = date2 - date1

print(difference.days)


# 4. Date and Time Formatting
now = datetime(2026, 11, 2, 21, 45, 10)

print(now.strftime("%d-%m-%Y"), now.strftime("%m/%d/%Y"))

print(now.strftime("%H:%M:%S"), now.strftime("%I:%M:%S %p"))


# 5. Add Weeks, Days and Hours
result = now + timedelta(weeks=1, days=6, hours=3)

print(result.strftime("%Y-%m-%d %H:%M:%S"))




