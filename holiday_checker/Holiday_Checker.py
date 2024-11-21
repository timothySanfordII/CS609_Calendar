import datetime

# Holidays database
holidays = {
    "01-01": "New Year's Day",
    "07-04": "Independence Day",
    "12-25": "Christmas",
    "11-11": "Veterans Day",
    "11-24": "Thanksgiving",
}


def get_day_of_week(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime("%A")


def is_holiday(month, day):
    date_key = f"{month:02d}-{day:02d}"
    return holidays.get(date_key, None)


def main():
    print("Enter a date to check (format: YYYY-MM-DD):")
    date_input = input()

    try:
        year, month, day = map(int, date_input.split('-'))
        day_of_week = get_day_of_week(year, month, day)
        holiday_name = is_holiday(month, day)

        print(f"The date you entered is: {date_input}")
        print(f"Day of the week: {day_of_week}")

        if holiday_name:
            print(f"Holiday: {holiday_name}")
        else:
            print("This date is not a holiday.")

    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")


if __name__ == "__main__":
    main()