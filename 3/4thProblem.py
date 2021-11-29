hours = int(input("How Many Hours were worked?"))
carssold = int (input("Total number of cars sold for the week?"))
basewage = 36.25
overtimewage = basewage * 1.5


if hours >= 37:
    overtimehours = hours - 37
    weeklywage = (basewage * 37) + (overtimehours * overtimewage)
else:
    weeklywage = basewage * hours

if carssold > 5:
    commission = (carssold - 5) * 200
else:
    commission = 0

totalwage = weeklywage + commission
print("The salary is", totalwage)