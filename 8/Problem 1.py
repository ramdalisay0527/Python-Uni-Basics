#pop and append
#identify iteration size which is 4 in the example

input1 = input("Input a list: ")
numbers = str.split(input1)
print(numbers)
firstnumber = numbers[0]
popped = numbers.pop(0)
numbers.append(popped)
print(numbers)

while numbers[0] != firstnumber:
    popped = numbers.pop(0)
    numbers.append(popped)
    print(numbers)