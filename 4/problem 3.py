number = int(input("Enter a Positive Number: "))
rows = 2*number-1

for i in range(1, (rows+1)//2+1):
    for j in range((rows+1)//2 - i):
        print(" ", end="")
    for k in range((i*2)-1):
        print("*", end="")
    print()

for i in range((rows+1)//2+1 , rows+1):
    for j in range(i - (rows+1)//2):
        print(" ", end="")
    for k in range((rows+1 - i)*2 - 1):
        print("*", end="")
    print()