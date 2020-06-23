#adding elements to a list
family = []
family.append('Hayden')
family.append('Nicole')
family.append('Bruce')
family.append('Lauren')
family.append('Sparky')
print(family[4])
#adding in a specific loction
family.insert(5,'Merlin')
print(family[5])

#Finding an element

if 'Nicole' in family :
    print('She is my mother')

#removing an element
family.insert(6,'Tim')
family.pop(6)
print(family)

#combinding lists
extendedFamily = ['Hope', 'Pa', 'Moemoe', 'Grandma', 'Papa', 'Erin', 'Brian']
wholeFamily = extendedFamily + family
print(wholeFamily)

#replication
monthInQuarter = [1,2,3] * 4
print(monthInQuarter)

#Equality and inequality testing
if [1,2,3]==[1,2,3] :
    print('True')
if [1,2,3] == [3,2,1] :
    print('False')
if [1,2,3] != [3,2,1] :
    print('True')

#Sum, Max and Min
numList = [12,45,98,45,67,32,59]
print(sum(numList))
print(min(numList))
print(max(numList))

#sorting
print(sorted(numList))

#copying lists
prices = list(numList)
print(prices)

#Slicing a list
#if you only want to use part of a list
people = family[0:4]
print(people)
pets = family[4:6]
print(pets)
otherFamily = wholeFamily[ :7]
print(otherFamily)
myFamily = wholeFamily[7:]
print(myFamily)
