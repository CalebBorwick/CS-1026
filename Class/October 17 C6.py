from random import randint
def printEvenValues(someList) :
    for el in someList :
        if el %2 == 0 :
            print(el,end=" ")
    print()

def printValuesAtEvenIndex(someList):
    for i in range(0, len(someList),2):
        print(someList[i], end= " ")

def returnFistAndLast(someList):
    return (someList[0], someList[len(someList)-1])

values = []
for i in range(10):
    values.append(randint(1,100))
print(values)





def myListMaster(listOfV) :
    listOdd = []
    listEven = []
    for value in listOfV :
        if value %2  == 0 :
            listEven.append(value)
        else :
            listOdd.append(value)
    print(listOdd)
    print(listEven)


x = myListMaster([4,5,7,5,4,2,2,3,4,5])
print(x)
