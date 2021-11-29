#better to have 5 functions because there are 5 lanugages
#split the function and check the leng if it's 1 2 or 3. if it is 2 then check if word is in list and if it's threee then the same, also check if the word is in the list
#check if value is purely an int
#dictionary
#gets, if the variable already has a value then simply update the value in the dictionary
#for input b function you will only be allowed to enter a digit
#adds function: c adds b meaning C will be 3 (check workshop for prior values of c and b)
#print, just print the variable value
#if value of variable doesnt exist then disb
#check if the print value is a variable or a number!!!!
#if print is just a number, then simply print the number
#syntax error if the program doesnt recognise the function at all. always check the string first and split then use **in
repldict = {}
replfunction = input("??? ")


def inputfunction(replfunction):
    inputfunctionstring = replfunction
    inputfunctionvalue = input("Enter a value for " +inputfunctionstring[1] + ": ")
    repldict[inputfunctionstring[1]] = int(inputfunctionvalue)

def getsfunction(replfunction):
    getsfunctionstring = replfunction
    getsfunctionvariable = getsfunctionstring[0]
    getsfunctionvalue = getsfunctionstring[2]
    getsvariablecheck = str.isdigit(getsfunctionstring[2])
    if getsvariablecheck == True:
        repldict[getsfunctionvariable] = int(getsfunctionvalue)
    elif getsvariablecheck == False:
        variableexistense = getsfunctionstring[2] in repldict
        if variableexistense == True:
            repldict[getsfunctionvariable] = repldict.get(getsfunctionvalue)
        else:
            print("not here")

def addsfunction(replfunction):
    addsfunctionstring = replfunction
    addsfunctionvariable = addsfunctionstring[0]
    addsfunctionvalue = addsfunctionstring[2]
    newvalue = int(repldict.get(addsfunctionvariable)) + int(repldict.get(addsfunctionvalue))
    repldict[addsfunctionvariable] = newvalue

def printfunctionvariable(replfunction):
    printfunctionstring = replfunction
    printfunctionvariable= printfunctionstring[1]
    checkvariableexistence = printfunctionvariable in repldict
    if checkvariableexistence == True:
        printvalue = repldict.get(printfunctionvariable)
        print(printfunctionvariable + " equals", printvalue)
    else:
        print(printfunctionvariable + " is undefined")

def printfunctionnumber(replfunction):
    printfunctionnumberstring = replfunction
    printfunctionnumber = printfunctionnumberstring[1]
    print(printfunctionnumber)



while replfunction != 'quit':
    stringreplfunction = str.split(replfunction)
    replfunctionlength = len(stringreplfunction)

    if replfunctionlength == 2:
        if stringreplfunction[0] == 'print':
            digit = str.isdigit(stringreplfunction[1])
            if digit == True:
                printfunctionnumber(stringreplfunction)
            elif digit == False:
                printfunctionvariable(stringreplfunction)
        elif stringreplfunction[0] == 'input':
            inputfunction(stringreplfunction)
        else:
            print("Syntax Error")

    elif replfunctionlength == 3:
        if stringreplfunction[1] == 'gets':
            getsvariablecheck = str.isdigit(stringreplfunction[0])
            if getsvariablecheck == True:
                print("Syntax Error")
            elif getsvariablecheck==False:
                getsfunction(stringreplfunction)
        elif stringreplfunction[1] == 'adds':
            addsfunction(stringreplfunction)
        else:
            print("Syntax Error")
    else:
        print("Syntax Error")
    replfunction = input("??? ")

print("Goodbye.")
#elif replfunctionlength == 2:

#elif replfunction == 3:
