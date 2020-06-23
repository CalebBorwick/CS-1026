#creating tables
table = []
rows = 5
columns = 8

for i in range(rows):
    rows = [0] *columns
    table.append(rows)

#ie Medals

countries = 8
medals = 3
count = [
    [0,3,0],
    [0,0,1],
    [0,0,1],
    [1,0,0],
    [0,0,1],
    [3,1,1],
    [0,1,0],
    [1,0,1]
]
medalCount = count[3][1]

for i in range(countries):
    for j in range(medals) :
        print("%8d" % count[i][j], end= "")
        print()

#adding rows
total = 0
for j in range(medals) :
    total = total + count[i][j]
#adding columns
total = 0
for i in range(medals) :
    total = total + count[i][j]


#Tables
myList = [[10,20],[30,40]]
print(myList[0])
print(myList[1])
#list nesting
print(myList[1][1])

