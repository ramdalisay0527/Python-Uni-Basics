year1 = int(input("Year 1?"))
year2 = int(input("year 2?"))
totaldays = 0


for y in range(year1, year2+1):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) == True:
        days = 366
        totaldays = totaldays + days
    else:
        days = 365
        totaldays = totaldays + days

print ("Number of days:", totaldays)
