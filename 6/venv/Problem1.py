words = input("Enter a string: ")

while str.isdigit(words) == False and words != "":
    words = str.lower(words)
    listofwords = words.split()
    listofwords.sort(reverse=True)
    print("Output:", end=" ")
    for i in listofwords:
        print(i, end=" ")
    print("")
    words = input("Enter a string: ")
