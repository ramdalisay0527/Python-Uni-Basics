x = int(input("Integer 1?"))
y = int(input("Integer 2?"))
z = int(input("Integer 3?"))

if y < x > z:
    big = x
    if y > z:
        medium = y
        small = z
    else:
        medium = z
        small = y
elif x < y > z:
    big = y
    if x > z:
        medium = x
        small = z
    else:
        medium = z
        small = x
elif x < z > y:
    big = z
    if x > y:
        medium = x
        small = y
    else:
        medium = y
        small = x

print("Sorted:", big, medium, small)