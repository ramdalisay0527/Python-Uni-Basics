import math

dimension1 = float(input("Enter room dimension 1 (m): "))
dimension2 = float(input("Enter room dimension 2 (m): "))

lengthwise = 0
widthwise = 0

def carpetneededlengthwise(a,b):
    print("Length= {:.3f}m".format(a))
    print("Width= {:.3f}m".format(b))
    lengthwise = math.ceil(a)
    widthwise = math.ceil(math.ceil(a/3.66)*b)
    print("Total length required lengthways:", lengthwise)
    print("Total length required widthways:", widthwise)


while dimension1 > 0 and dimension2 > 0:

    if (dimension1 > dimension2):
        carpetneededlengthwise(dimension1,dimension2)
    elif(dimension2 > dimension1):
        carpetneededlengthwise(dimension2,dimension1)

    dimension1 = float(input("Enter room dimension 1 (m): "))
    dimension2 = float(input("Enter room dimension 2 (m): "))
