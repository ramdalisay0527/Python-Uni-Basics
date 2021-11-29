#for loop and traverse the file record by record
# for each loop identify the meeting number
#you need a lis of name
#outside forloop you need an list for infection
#have a for loop to traverse the name list if name end with "*" then append the name to the infection list
#get the person to the lift (current_index + length of list  - 1) % length of list
# you have  2 ifs and the first ifs will only be used once but second will be done all the time
filename = input("Enter File name: ")
f1 = open(filename)
global bookfeverlist
bookfeverlist = []

for line in f1: #traverses lines of document

    attendees = str.split(line)
    meetingno = int(attendees[0])

    if len(bookfeverlist) == 0:
        for attendee in attendees: #traverses the names in every line  being read
            if attendee.endswith("*"):
                attendeename = attendee[:-1]
                bookfeverlist.append(attendeename)
                indexofattendee = attendees.index(attendee)

                if indexofattendee == 1:
                    bookfeverlist.append(attendees[-1])
                    bookfeverlist.append(attendees[indexofattendee + 1])
                elif indexofattendee == (len(attendees) - 1):
                    bookfeverlist.append(attendees[1])
                    bookfeverlist.append(attendees[indexofattendee - 1])
                else:
                    bookfeverlist.append(attendees[indexofattendee - 1])
                    bookfeverlist.append(attendees[indexofattendee + 1])
    else:
        for attendee in attendees: #traverses the names in every line  being read
             if bookfeverlist.count(attendee) > 0:

                indexofattendee = attendees.index(attendee)

                if indexofattendee == 1:
                    bookfeverlist.append(attendees[indexofattendee + 1])
                    bookfeverlist.append(attendees[-1])
                    break
                elif indexofattendee == (len(attendees) - 1):
                    bookfeverlist.append(attendees[1])
                    bookfeverlist.append(attendees[indexofattendee - 1])
                    break

                else:
                    if bookfeverlist.count(attendees[indexofattendee + 1]) > 0:
                        bookfeverlist.append(attendees[indexofattendee - 1])
                        bookfeverlist.append(attendees[indexofattendee + 2])
                        break
                    else:
                        bookfeverlist.append(attendees[indexofattendee - 1])
                        bookfeverlist.append(attendees[indexofattendee + 1])
                        break

    if bookfeverlist != []:
        print(meetingno, end=" ")
        for i in range(len(bookfeverlist)):
                print(bookfeverlist[i], end=" ")
        print(len(bookfeverlist))


