values= [1,2,3,4,5,6,7,8,9]

#using lists with functions
def sum(values) :
    total = 0
    for elements in values :
        total = total + elements
    return total
print(sum(values))

#modfying list elements
def multiply(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i] * factor
    return multiply(values)
print(values)

#Returning list from functions
def squares(n) :
    results=[]
    for i in range(n) :
        results.append(i*i)
    return results
print(squares(3))

#Tuples
#cannot change the contents
#use () NOT []
triple = 5, 10, 15

#Returning Multiple Values
#Function definition
def readDate() :
    print('Enter a date')
    month = int(input('Month: '))
    day = int(input('Day: '))
    year = int(input('Year: '))
    return (month, day, year)
#function call - assign entire value to a tuple
date = readDate()
print(date)

