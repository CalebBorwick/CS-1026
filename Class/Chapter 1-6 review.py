#Prints
#print functions
#errors
    #logical and syntax errors
    #finding logic errors
#variable definition

#chapter6

import random
list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
for i in range(10):
    list0.append(random.randint(0,101))
print(list0)

count = 0
for i in list0:
    if count % 2 == 0:
        list1.append(i)
    count = count + 1
print(list1)

for i in list0:
       if i %2 == 0 :
        list2.append(i)
print(list2)

for i in list0 :
    list3.append(i)
print(list3[::-1])

for i in list0 :
    if i == list0[0] or i == list0[-1]:
        list4.append(i)
print(list4)
