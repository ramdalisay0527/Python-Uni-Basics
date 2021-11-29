word = input("String: ")

while word != "" and word.count('g') != 0:

    gindex = int(word.index('g'))
    if len(word) == 1:
        print("Happy? False")
        word = input("String: ")
    elif word[gindex+1] == 'g' or word[gindex-1] == 'g':
        print("Happy? True")
        word = input("String: ")
    else:
        print("Happy? False")
        word = input("String: ")
