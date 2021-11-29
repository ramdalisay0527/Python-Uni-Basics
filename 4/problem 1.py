positivenumber = 0
number = int(input("Enter a Number: "))

while number != 0:
    if number > 0:
        positivenumber = positivenumber + 1
        number = int(input("Enter a Number: "))

    elif number < 0:
        number = int(input("Enter a Number: "))


print(positivenumber, "Positive numbers were entered.")