filename = input("File Name: ")
f1 = open(filename)
counter = 0
writecounter = 0

for line in f1:
    counter += 1

f1 = open(filename)

for line in f1:

    if writecounter == 0 or writecounter == 1 or writecounter == counter - 1 or writecounter == counter - 2:
        print(line, end="")
        writecounter += 1
    else:
        writecounter += 1
