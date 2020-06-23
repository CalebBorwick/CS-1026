count = 1
total = 0
smallest = 0

intNumber = int(input("How many numbers would you like to input: "))
variable = int(input('Please enter a value: '))
total = total + variable

while count < intNumber :
    value = int(input('Please enter a value: '))
    count = count + 1
    total = value + total
    if value < variable :
        smallest = value
    if value > variable :
        largest = value
    average = total/(count)


print('The average is',round(average, 0))
print('The minimum value is', smallest)
print('The lagest value is', largest)
print('The range is', largest - smallest)
