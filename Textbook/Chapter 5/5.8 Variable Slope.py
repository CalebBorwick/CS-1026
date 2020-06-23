#Global variable
balance = 10000
def withdraw(amount) :
    global balance
    if balance >= amount:
        balance = balance - amount


#Same Variable multi times
def main() :
    result = square(3) +square(4)
    print(result)
def square(n) :
    result = n*n
    return result
main()

#Error problem
#def main() :
    #sideLength = 10
    #result = cubeVolume()
    #print(sum)

#def cubeVolume():
   # return sideLength ** 3

#main()
