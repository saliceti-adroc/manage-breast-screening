"""
Format and dates and times in a way consistent with
the NHS service manual's content guide:
https://service-manual.nhs.uk/content/numbers-measurements-dates-time
"""

from datetime import date, datetime


def format_date(value):
    """
    Format a date

    >>> from datetime import date
    >>> format_date(date(2025, 1, 1))
    '1 January 2025'
    """
    return value.strftime("%-d %B %Y")


def format_relative_date(value: datetime | date):
    """
    Format a date relative to today as a number of days.
    """
    if isinstance(value, datetime):
        value = value.date()

    today = date.today()
    days = (value - today).days

    if days < -1:
        return f"{abs(days)} days ago"
    elif days == -1:
        return "yesterday"
    elif days == 0:
        return "today"
    elif days == 1:
        return "tomorrow"
    else:
        return f"in {days} days"


def format_date_time(value):
    """
    Format a datetime

    >>> from datetime import datetime
    >>> format_date_time(datetime(2025, 12, 31, 12, 30))
    '31 December 2025, 12:30pm'
    """
    date_part = format_date(value)
    time_part = format_time(value)
    return f"{date_part}, {time_part}"


def format_time(value):
    """
    Format a time on a 12-hour clock, with special cases for midday and midnight.

    >>> from datetime import time
    >>> format_time(time(9, 15))
    '9:15am'

    >>> format_time(time(13, 30))
    '1:30pm'

    >>> format_time(time(12))
    'midday'

    >>> format_time(time(0))
    'midnight'
    """
    if value.minute == 0:
        if value.hour == 0:
            return "midnight"
        if value.hour == 12:
            return "midday"
        return value.strftime("%-I%p").lower()

    return value.strftime("%-I:%M%p").lower()


def format_time_range(value):
    """
    Format a dictionary containing "start_time" and "end_time"

    >>> from datetime import time
    >>> format_time_range({'start_time': time(12, 00), 'end_time': time(12, 45)})
    'midday to 12:45pm'
    """
    start_time = format_time(value["start_time"])
    end_time = format_time(value["end_time"])
    return f"{start_time} to {end_time}"
