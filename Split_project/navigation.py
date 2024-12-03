import calendar
import holidays

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
    cal = calendar.TextCalendar()
    us_holidays = holidays.US(years=year)
    month_holidays = [holiday for holiday in us_holidays if holiday.year == year and holiday.month == month]
    cal_str = cal.formatmonth(year, month)

    # Create a dictionary to store the holiday names for each day
    holiday_dict = {}
    for holiday in month_holidays:
        holiday_date = holiday
        holiday_name = us_holidays.get(holiday)
        holiday_dict[holiday_date.day] = holiday_name

    # Split the calendar string into lines
    lines = cal_str.split('\n')

    # Iterate over each line and replace day numbers with holiday names
    for i, line in enumerate(lines):
        if i >= 2:  # Skip the header lines
            days = line.split()
            for j, day in enumerate(days):
                if day.isdigit():
                    day_num = int(day)
                    if day_num in holiday_dict:
                        holiday_name = holiday_dict[day_num]
                        lines[i] = lines[i].replace(str(day_num), f"{day_num:2d}*")
                        lines[i] = lines[i].replace(f"{day_num:2d}*", f"{holiday_name[:2]}.")

    # Join the modified lines back into a single string
    cal_str = '\n'.join(lines)

    return cal_str