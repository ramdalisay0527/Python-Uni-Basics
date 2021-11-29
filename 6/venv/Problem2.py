firstlist = input("List1: ")
secondlist = input("List2: ")

def sum(indexone,indexlast):
    sum = indexone + indexlast
    return sum

while firstlist != "" or secondlist !="":
    firstnumberlist = firstlist.split()
    secondnumberlist = secondlist.split()


    if len(secondnumberlist) == 1 or len(firstnumberlist) == 1:
        sumsecond = int(secondnumberlist[0])
        sumfirst = int(firstnumberlist[0])
    else:
        sumsecond = sum(int(secondnumberlist[0]), int(secondnumberlist[-1]))
        sumfirst = sum(int(firstnumberlist[0]), int(firstnumberlist[-1]))

    if sumfirst > sumsecond:
        print("Output:", sumfirst)
        firstlist = input("List1: ")
        secondlist = input("List2: ")
    elif sumsecond > sumfirst:
        print("Output:", sumsecond)
        firstlist = input("List1: ")
        secondlist = input("List2: ")
    elif sumfirst == sumsecond:
        print("Output:Same")
        firstlist = input("List1: ")
        secondlist = input("List2: ")