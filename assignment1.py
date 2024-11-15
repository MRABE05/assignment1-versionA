#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: "Ma Therese Dominique Rabe"
The python code in this file (assignment1.py) is original work written by
"Ma Therese Dominique Rabe". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

from datetime import datetime

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    "Returns the maximum number of days for a given month, accounting for leap years in February"
    if month in {4, 6, 9, 11}:  # April, June, September, November
        return 30
    elif month == 2:  # February
        return 29 if leap_year(year) else 28
    else:
        return 31

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for year after 1582.
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = 1  # reset to 1 if tmp_day exceeds this month's max
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year += 1
    else:
        to_month = tmp_month

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def valid_date(date: str) -> bool:
    "Check validity of date and return True if valid"
    try:
        # Try transfer the date to check its validity
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    if not (valid_date(start_date) and valid_date(stop_date)):
        raise ValueError("Invalid date format. Dates must be in YYYY-MM-DD format.")

    weekend_count = 0
    current_date = start_date

    while current_date <= stop_date:
        year, month, day = map(int, current_date.split('-'))
        day_name = day_of_week(year, month, day)
        if day_name in ['sat', 'sun']:
            weekend_count += 1
        current_date = after(current_date)

    return weekend_count

# Output
print(day_count("2024-11-01", "2024-11-14")) 
