# Basics
for i in range(0, 151, 1):
    print (i)

# Multiples of 5
for i in range(5, 1005, 5):
    print (i)

#Counting the dojo way
for i in range(1, 101, 1):
    if i % 10 == 0:
        print ("Coding")
    elif i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)
    

#Whoa. That Sucker's Huge
oddsum = 0
for i in range(0, 500000, 1):
    if(i % 2 == 1):
        print(i)
        oddsum = oddsum + i
print("The sum of the odd numbers added is {}".format(oddsum))

#Countdown by four
for i in range(2018, 0,-4):
    print(i)

#Flexible Counter
lownum = 2
highnum = 9
mult = 3
for i in range(lownum, highnum, mult):
    if i % mult != 0:
        print(i + 1)