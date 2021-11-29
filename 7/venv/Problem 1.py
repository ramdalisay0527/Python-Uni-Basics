file1 = input("Source File Name: ")
file2 = input("Target File Name: ")

f1 = open(file1)
f2 = open(file2, mode='w')
counter = 0

line = f1.readline()


while line != "":
    if line == '\n':
        counter += 1
        line = f1.readline()
    else:
        f2.write(line)
        line = f1.readline()

print("Lines removed:", counter)




