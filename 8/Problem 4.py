
list3 = [] #list for sorted numbers from both list
list1counter = 0
list2counter = 0

list1 = input("List 1: ")
list1numbers = str.split(list1)
list1numbersint = [int(i) for i in list1numbers] #i converted the list from string to int
list1numbersintsorted = sorted(list1numbersint, reverse=True)
lengthlist1 = len(list1numbersint) - 1

while list1 != "":

    list2 = input("List 2: ")
    list2numbers = str.split(list2)
    list2numbersint = [int(i) for i in list2numbers]
    list2numbersintsorted = sorted(list2numbersint, reverse=True)
    lengthlist2 = len(list2numbersint) - 1


    while list1counter <= lengthlist1 and list2counter <= lengthlist2:
        if list1numbersintsorted[list1counter] > list2numbersintsorted[list2counter]:
            list3.append(list1numbersintsorted[list1counter])
            list1counter += 1
        elif list2numbersintsorted[list2counter] > list1numbersintsorted[list1counter]:
            list3.append(list2numbersintsorted[list2counter])
            list2counter += 1
        elif list1numbersintsorted[list1counter] == list2numbersintsorted[list2counter]:
            list3.append(list1numbersintsorted[list1counter])
            list3.append(list2numbersintsorted[list2counter])
            list1counter += 1
            list2counter += 1
    while list1counter <= lengthlist1:
            list3.append(list1numbersintsorted[list1counter])
            list1counter += 1
    while list2counter <= lengthlist2:
            list3.append(list2numbersintsorted[list2counter])
            list2counter += 1

    print(list3)
    list3 = []
    list1counter = 0
    list2counter = 0

    list1 = input("List 1: ")
    list1numbers = str.split(list1)
    list1numbersint = [int(i) for i in list1numbers]
    list1numbersintsorted = sorted(list1numbersint, reverse=True)
    lengthlist1 = len(list1numbersint) - 1

