#filling a list
values = []
for i in range(0,10) :
    values.append(i*i)
print(values)

#combinding list elements
result = 0.0
for elements in values :
    result = result+elements
print(result)

#Max and Min
largest = values[0]
for i in range(1,len(values)) :
    if values[i] > largest :
        largest = values[i]
print(largest)

smallest = values[0]
for i in range(1,len(values)) :
    if values[i] < smallest :
        smallest = values[i]
print(smallest)

#linear search
limit = 100
pos = 0
found = False
while pos < len(values) and not found :
    if values[pos] >limit :
        found = True
    else :
        pos = pos + 1
if found :
    print('Found at position', pos)
else :
    print('Not found')

#collecting matches
limit = 36
result = []
for elements in values :
    if (elements > limit) :
        result.append(elements)
print(result)

#counting matches
limit = 36
counter = 0
for elements in values :
    if (elements > limit) :
        counter = counter +1
print(counter)

#Removing matches - wont work
#i = 0
#while i < len(words) :
   # word = words[i]
   # if len(word) < 4 :
        #words.pop(i)
    #else :
      #  i = i + i

#switching list variables
temp = values[4]
values[4] = values[7]
values[7] = temp
print(values)

#reading input
values = []
print('Enter a values, or q to quit')
userinput = input("")
while userinput.upper() != 'Q' :
    values.append(float(userinput))
    userinput = input("")
