#find common element in the list
#use list
# list should not contain duplicates
#create 3 lists and check if value is in list 1,2 or 3
list1 = input("List 1: ")
while list1 != []:

    list1numbers = str.split(list1)

    list2 = input("List 2: ")
    list2numbers = str.split(list2)

    list3numbers = []

    for i in list1numbers:
        if list2numbers.count(i) > 0:
            if list3numbers.count(i) < 1:
                list3numbers.append(i)

    print(list3numbers)
    list1 = input("List 1: ")