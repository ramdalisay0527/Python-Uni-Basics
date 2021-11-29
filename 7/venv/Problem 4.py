filename = input("File Name: ")
f1 = open(filename)

characters = 0
charline = 0
words = 0
wordsline = 0
wordslinecount = 0
wordslinecountsplit= ""
lines = 0


for line in f1:
    charline = len(line)
    characters += charline
    lines += 1

print("Characters:", characters)

f1same = open(filename)

while wordsline != "":
    wordsline = f1same.readline()
    wordslinecount = len(wordsline.split())
    words +=wordslinecount

print("Words:", words)
print("Lines:", lines)


