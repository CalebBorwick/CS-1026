#used for sum and average values
#Counting matches
#prompting until match is found
#Max and Min problems
#Comparing adjacent values

#comparing adjacent values ecample
value = int(input('Enter a value: '))
inputStr = input('Enter a value: ')
while inputStr != "" :
    previous = value
    value = int(inputStr)
    if value == previous :
        print('Duplicate input')
    inputStr = input('Enter a value: ')

#min example
smallest = int(input('Enter a value: '))
inputStr = input('Enter a value: ')
while inputStr != "" :
    value = int(inputStr)
    if value < smallest :
        smallest = value
    inputStr = input('Enter a value: ')
print(smallest)


#max example
largest = int(input('Enter a value: '))
inputStr = input('Enter a value: ')
while inputStr!="" :
    value = int(inputStr)
    if value > largest :
        largest = value
    inputStr = input('Enter a value: ')
print(largest)

#prompt until match is found example
valid = False
while not valid :
    value = int(input('Enter a positive value < 100: '))
    if value > 0 and value <100 :
        valid = True
    else :
        print('Invalid input')

#counting matches example
negatives = 0
inputStr = input('Enter a value: ')
while inputStr != "" :
    value = int(inputStr)
    if value < 0 :
        negatives = negatives + 1
    inputStr = input('Enter a value: ')
print('Thats were', negatives, "negative values")

#Sum example
total = 0
inputStr = input('Enter a value: ')
while inputStr != "" :
    value = float(inputStr)
    total = total +value
    inputStr = input('Enter a value ')
print(total)

#average example
total = 0.0
count = 0
inputStr = input('Enter value: ')
while inputStr != "" :
    value = float(inputStr)
    total = total + value
    count = count + 1
    inputStr = input('Enter a value: ')
if count >0 :
    average = total /count
else :
    average = 0.0

print(average)
