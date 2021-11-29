sentence = input("Input a string? ")

def convert(sent):
    for i in (sentence):
        if i.isdigit() == True:
            i = "_"
            print(i, end="")
        else:
            print(i, end="")
    print()

while sentence != "":
    convert(sentence)
    sentence = input("Input a string? ")