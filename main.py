import calendar


def generate_calendar(year, month):
    # Create a Calendar object
    cal = calendar.monthcalendar(year, month)

    # Get the month name
    month_name = calendar.month_name[month]

    # Create the calendar header
    header = f"{month_name} {year}\n"
    header += "Mo Tu We Th Fr Sa Su\n"

    # Generate the calendar body
    body = ""
    for week in cal:
        for day in week:
            if day == 0:
                body += "   "
            else:
                body += f"{day:2d} "
        body += "\n"

    # Combine header and body
    full_calendar = header + body
    return full_calendar


# Example usage
print(generate_calendar(2024, 9))

