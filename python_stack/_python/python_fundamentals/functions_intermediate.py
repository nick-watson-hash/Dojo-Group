import random
def randInt(min=0, max=100 ):
    num = random.random() * max
    num = round(num)
    return num
print(randInt())
print(randInt(max=78))
print(randInt(min=25))
print(randInt(min=2, max=50))