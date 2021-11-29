filename = input("file name: ")
f1 = open(filename)

for scores in f1:
    #line = f1.readline().split()
    line = scores.split()
    linecount = len(line)
    sum = 0
    average = 0
    xint = 0

    for x in line:
        xint = int(x)
        sum += xint

    average = sum/linecount
    print("the average is:", average)
