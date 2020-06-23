#Input and output


costOfYourPhone = input('How much did you pay for your Phone? ')
phonePrice = (costOfYourPhone)
phoneType = input('What type of phone? ')
print ("dont you feel silly for paying", costOfYourPhone, "dollars for just a", phoneType)

favMovie = input('What is your favourite movie? ')
print (favMovie)

firstName = input ('Please Enter Your First Name: ')
lastName = input ('Please Enter Your Last Name: ')
name = firstName + lastName

print('Welcome ', name)

#convert pennies to dallars and cents
pennies = 2378
dollars = pennies // 100 #number of dollars
cents = pennies % 100 #number of cents
print ('I have', dollars, 'dollars', 'and', cents, 'cents')

#naming game
first = input("Enter your first name: ")
second = input("Enter your last first name: ")
initials = first[0] + "&" + second[0]
print(initials)

#price per ounce
cansPerPack = 6
userInput = input("Enter price for sixpack: ")
packPrice = float(userInput)
userInput = input("Enter volume per can: ")
canVolume = float(userInput)
packVolume = canVolume * cansPerPack
pricePerOunce = packPrice / packVolume
print("price per ounce: %8.2f" % pricePerOunce)

#string Methods
time = "it is twelve"
len(time)
print (len(time))

str1 = "Kemi"
print (str1.upper())
print (str1)

str1 = "Today is not a good day"
str2 = str1.replace ("not", "really")
print (str2)

value1 = '1234'
print (value1 * 2)
value1 = int(value1)
print (value1*2)


firstName = input ('Please Enter Your First Name: ')
lastName = input ('Please Enter Your Last Name: ')
name = firstName + lastName

print('Welcome ', name)
