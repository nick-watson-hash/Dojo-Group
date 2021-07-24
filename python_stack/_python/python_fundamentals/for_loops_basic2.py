#Biggie Size
def bs():
        lst = list(input("Enter multiple positive and negative numbers: ").split())
        lst = list(map(int, lst))
        for x in range(len(lst)):
            if lst[x] < 0:
                print("big")
            else:
                lst[x] > 0
                print(lst[x])
bs()

#Count Positives
def count():
        lst = list(input("Enter multiple positive and negative numbers: ").split())
        lst = list(map(int, lst))
        print(*lst)
        for x in range(len(lst)):
            if lst[x] == lst[-1]:
                print(abs(lst[-1]))
            else: print(lst[x])
count()

#Sum total
def count():
        lst = list(input("Enter multiple positive and negative numbers: ").split())
        lst = list(map(int, lst))
        counter = 0
        for x in range(len(lst)):
            if lst[x] == lst[x]:
                counter += lst[x]
        print(counter)
count()

#Average
def avg():
        lst = list(input("Enter multiple numbers: ").split())
        lst = list(map(int, lst))
        counter = 0
        for x in range(len(lst)):
            if lst[x] == lst[x]:
                counter += lst[x]
                avg = counter / len(lst)
        return (avg)
avg()

#Length
def length():
            lst = list(input("Enter multiple numbers: ").split())
            counter = 0
            for x in range(len(lst)):
               if lst[x] == lst[x]:
                   counter += 1
            return(print(counter))
length()

#Minimum
def mnm():
        lst = list(input("Enter multiple numbers: ").split())
        for x in range(len(lst)):
            if lst[x] == lst[x]:
                pass
        smallest = min(lst)
        print(smallest)
mnm()

#Maximum
def mxm():
        lst = list(input("Enter multiple numbers: ").split())
        for x in range(len(lst)):
            if lst[x] == lst[x]:
                pass
        biggest = max(lst)
        print(biggest)
mxm()

#Ultimate analysis
def ua():
    sum1 = 0
    avgset = 0
    lst = list(input("Enter multiple numbers: ").split())
    lst = list(map(int, lst))
    for x in range(len(lst)):
        if lst[x] == lst[x]:
            avgset += lst[x]
            avg = avgset / len(lst)
            sum1 += lst[x]
    dict1 = {
        "SumTotal": sum1,
        "Average": avg,
        "Minimum" : min(lst),
        "Maximum" : max(lst),
        "Length" : len(lst),
        }
    return(dict1)
ua()

# Reverse List
def rev():
    lst = list(input("Enter multiple numbers: ").split())
    for x in range(len(lst)):
        backword = lst.reverse()
    (print(lst))
rev()