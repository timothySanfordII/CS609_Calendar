def Event(day, month, year):
    #For 10, and June: Today is 10 of June
    print(f"Today is {day} of {month}, {year}.)
    #Calls the function defined elsewhere to determine day of week.
    DayOfWeekFunction(day, month, year)
    #Calls the function defined elsewhere to determine if
    #this particular day and month is a holiday
    IsHolidayFunction(day, month, year)

    #After all the functions are executed, output may look something
    #like:
    #Today is 1 of January, 2024. Today is Monday.
    #Happy New Year!

    #day and month and year are used in all functions definied elsewhere



