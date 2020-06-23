#Problem 1
values = [8,7,8.5,9.5,7,5,10]
smallestPos = 0
for i in range(1,len(values)):
    if values[i] < values[smallestPos] :
        smallestPos = i
print(values[smallestPos])
