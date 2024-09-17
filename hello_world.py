def calDayOfWeek(day, month, year):
    normalYear = [0,3,3,6,1,4,6,2,5,0,3,5]
    newYear = year-1
    dayOftheweek = (day+normalYear[month-1]+5*(newYear%4)+4*(newYear%100)+6*(newYear%400))%7
    print("function works %d %d %d the day %d" %(day, month, year, dayOftheweek))

print("hello world")