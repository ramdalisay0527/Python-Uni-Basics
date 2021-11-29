word = input("Input a string: ")
shortestword = word
newword = ""

while newword.startswith("A") == False:
    newword = input("Input a string: ")

    if len(newword) < len(word):
        shortestword = newword


print ("Shortest was: ", shortestword)