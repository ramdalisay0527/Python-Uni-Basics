# B3 coordinates is (0.5, 1)
# y 24 = 12, 11.5
# (coordinate minus 1) * .5 = coordinate number
# coordinateso of the problem  (1,0.5) (0.5,2) (12,12)
#import math library because you need square root
#sqrt((1-0.5)*(1-0.5)+(0.5-2)*(0.5-2))
#use str1 = 'B25' , str1[0], str[1:3] to extract key and value
import math
letterscoordinate = {'A':0 , 'B' : 0.5, 'C':1.0, 'D': 1.5, 'E': 2, 'F': 2.5, 'G': 3, 'H': 3.5, 'I': 4, 'J': 4.5, 'K': 5, 'L': 5.5, 'M': 6, 'N': 6.5, 'O': 7, 'P': 7.5, 'Q': 8, 'R': 8.5, 'S': 9, 'T': 9.5, 'U': 10, 'V': 10.5, 'W': 11, 'X': 11.5, 'Y': 12, 'Z': 12.5}
numberscoordinate = {'1':0 , '2' : 0.5, '3':1, '4': 1.5, '5': 2, '6': 2.5, '7': 3, '8': 3.5, '9': 4, '10': 4.5, '11': 5, '12': 5.5, '13': 6, '14': 6.5, '15': 7, '16': 7.5, '17': 8, '18': 8.5, '19': 9, '20': 9.5, '21': 10, '22': 10.5, '23': 11, '24': 11.5, '25': 12, '26': 12.5}

dictofnumbersforroot = {}
dictofdistances={}

references = input("Enter trip reference map: ")
inputcoordinatesstring = str.split(references)
lengthcoordinates = len(inputcoordinatesstring)

for c in range(lengthcoordinates):
    coord = inputcoordinatesstring[c]
    lettercoord = coord[0]
    numbercoord = coord[1:3]

    if lettercoord in letterscoordinate and numbercoord in numberscoordinate:
        letterequivalent = letterscoordinate.get(lettercoord)
        numberequivalent = numberscoordinate.get(numbercoord)
        dictofnumbersforroot[c] = [letterequivalent, numberequivalent]
    else:
        print("Bad Reference: ", end=' ')
        print(coord)
        exit()




#print(dictofnumbersforroot)
lengthofdicofnumberforroot = len(dictofnumbersforroot)

for cc in range(lengthofdicofnumberforroot):
    distance = 0
    coordinates1 = dictofnumbersforroot[cc]
    if cc < lengthofdicofnumberforroot - 1:
        coordinates2 = dictofnumbersforroot[cc + 1]
    else:
        break

    distance = math.sqrt(((coordinates2[0] - coordinates1[0])*(coordinates2[0] - coordinates1[0])) + ((coordinates2[1] - coordinates1[1])*(coordinates2[1] - coordinates1[1])))
    #print(distance)
    dictofdistances[cc] = distance

#print(dictofdistances)
lengthofdistancesdictionary = len(dictofdistances)
sumofdistance = 0

for d in range(lengthofdistancesdictionary):
    sumofdistance += dictofdistances.get(d)
print("Total distance = ", end=' ')
print('{:.1f}'.format(sumofdistance), end=' ')
print("km")