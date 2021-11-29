number = int(input("Enter a Positive Number: "))
rows = 2*number-1


for i in range(1, rows+1, 2):
    spaces1 = (rows - i) // 2
    print(" "*spaces1 + "*" * i, end="\n")

for i in range(rows-2, 0, -2):
    spaces2 = (rows - i) // 2
    print(" "*spaces2 + "*" * i, end="\n")