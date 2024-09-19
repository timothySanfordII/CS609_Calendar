
// V added test.py file

// Anthonys dayclass code
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

#Tommy

def generate_calendar(year, month):
    # Create a Calendar object
    cal = calendar.monthcalendar(year, month)

    # Get the month name
    month_name = calendar.month_name[month]

    # Create the calendar header
    header = f"{month_name} {year}\n"
    header += "Mo Tu We Th Fr Sa Su\n"


print("Reminder emails sent successfully.")

//Alex's code
def calDayOfWeek(day, month, year):
    normalYear = [0,3,3,6,1,4,6,2,5,0,3,5]
    newYear = year-1
    dayOftheweek = (day+normalYear[month-1]+5*(newYear%4)+4*(newYear%100)+6*(newYear%400))%7
    print("function works %d %d %d the day %d" %(day, month, year, dayOftheweek))

//calling alexs calDayOfWeek
calDayOfWeek(17,9,2023)

