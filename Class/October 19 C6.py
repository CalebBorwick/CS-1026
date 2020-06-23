#Rapid fire pulse check
#1 - B

#2 - c
values= [1,2,3,4,5]
moreValues = values
moreValues[3] = 6
print(values)

#3 - B
states = ['Alaska', 'Hawaii', 'Florida','Maine','Ohio', 'Florida']
removedValue = states.pop(3)
print(removedValue)

#4 - C
value = ['Q','W','E','R','T','Y']
print(value[2:4])

#Tables
myList = [[10,20],[30,40]]
print(myList[0])
print(myList[1])
#list nesting
print(myList[1][1])

myList[0].append(25)
print(myList[0])

for row in myList:
    for cell in row:
        print(cell, end=" ")


#pulse check

numlist = [[10,20,30],[98,99]]
print(numlist[1][1])
print(numlist[0])


#creating tables
table = []
rows= 5
columns = 8
for i in range(rows):
    rows = [0]*columns
    table.append(row)
