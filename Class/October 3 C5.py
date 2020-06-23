#pulse check


#summary activity
from random import  randint
def generateRandom(low, high):
    total = 0
    for i in range(10):
        x= randint(low,high)
        print (x)
        total = total + x
    return total
myTotal = generateRandom(10,100)
print('when i run it it is', myTotal)


#reusable function
def main():
    print('Please enter a time: hours, then minutes')
    hours = readIntBetween(0,23)
    minutes = readIntBetween(0,59)
    print('You entered %d hours and %d minutes' % (hours, minutes))

def readIntBetween(low,high) :
    value = int(input('Enter a value betwen '+ str(low) + ' and ' + str(high) + ':'))
    while value < low or value > high :
        print('Error: Value out of range')
        value = int(input('Enter a value betwen '+ str(low) + ' and ' + str(high) + ':'))
    return value

main()
#pulse check
def main():
    a = 2
    doubleIt(a)
    print(a)
def doubleIt (x) :
    return x * 2
main()

#Return Stataments
def main() :
    print('Volume', pVolume(9,10))
    print('Expected: 300')
    print('Volume', pVolume(1,10))
    print('Expected: 0')
def pVolume (base,height) :
    baseArea = base * base
    return height * baseArea / 3
main()

#The main value
def main() :
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)
    print("A cube with side lengths 2 has volume", result1)
    print("A cube with side lengths 10 has volume", result2)

def cubeVolume(sidelength) :
    volume = sidelength ** 3
    return volume

main()

# pulse check
from random import randint
total = 0
i = 0

while total <= 100 :
    x= randint(15,30)
    print(x)
    total = x + total
    i = i + 1

print('The total is', total)
print('The average is', total/i)
print('The number of random numbers used is', i)


