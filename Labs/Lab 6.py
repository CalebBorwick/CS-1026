#Part 2


from random import randint

list = []
counter = 0
while counter < 20 :
    num = randint(1,100)
    list.append(num)
    counter = counter + 1
print(list)
print(sorted(list))
#or
#list.sort()
#print(list)

#Part 1
numList =[]
count= 0
while count < 10 :
    value = int(input('Enter a value: '))
    if value not in numList:
        numList.append(value)
        count = count + 1

print(numList)

