import calendar

def prev_month(year, month):
    month -= 1
    if month < 1:
        month = 12
        year -= 1
    return year, month

def next_month(year, month):
    month += 1
    if month > 12:
        month = 1
        year += 1
    return year, month

def get_calendar(year, month):
    return calendar.TextCalendar().formatmonth(year, month)