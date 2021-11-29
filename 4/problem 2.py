number = int(input("Enter a number:"))
F0 = 0
F1 = 1
counter = 2
print(F0, F1, end=" ")

while counter < number:
    if counter % 4 == 0:
        print("")
        F2 = F0 + F1
        print(F2, end=" ")
        F0 = F1
        F1 = F2
        counter += 1
    else:
        F2 = F0 + F1
        print(F2, end=" ")
        F0 = F1
        F1 = F2
        counter += 1






