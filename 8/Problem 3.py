#read each line and compare the difference between two number
# start the loop from the end and work your way to the start of the list and compare the differences
file1 = input("Source FileName: ")
f1 = open(file1)


for numbers in f1:
    numbersline = numbers.split()
    counter = len(numbersline) - 1
    difference = 0
    differencecomparison = 0
    diff = ""


    difference = int(numbersline[counter]) - int(numbersline[counter-1])
    counter -= 1
    differencecomparison = difference

    while counter > 0:
        difference = int(numbersline[counter]) - int(numbersline[counter - 1])

        if difference - differencecomparison == 0:

            diff = "True"
            differencecomparison = difference

            counter -= 1
        else:
            diff = "False"
            differencecomparison = difference
            counter -= 1
            break

    for num in range(len(numbersline)):
        print(numbersline[num], end=' ')
    print(diff)
