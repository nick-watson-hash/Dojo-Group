#Countdown
def cd():
    countDown = int(input("Enter a number to countdown from: "))
    for x in range(countDown, -1, -1):
        print (x)
cd()

#Print and Return
def par():
    enter = int(input("Enter a number: "))
    returned = int(input("Enter another number: "))
    numbers = [enter, returned]
    print ("Print: ", enter)
    return(print("Returned: ", returned))
par()

#First plus Length
def fpl():
    msg = list(input("Enter multiple numbers: "))
    msg = list(map(int, msg))
    msgl = (len(msg))
    print(msgl)
    return (print(msgl + msg[0]))
fpl()

#Values greater than second
def vgts():
    msg = list(input("Enter multiple numbers between 0-9: "))
    counter = 0
    for x in msg:
        if x > msg[2]:
            counter +=1
            print(x)
    if counter < 2:
        print("False")
    return(print(counter))
vgts()

#This Length that value
def tltv():
    msg = int(input("Enter the length of the list: "))
    msg2 = int(input("Enter the value: "))
    list = []
    for x in range(0, msg):
        list.extend(msg2)
        print(list)
tltv()
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

#     Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)