#Pulse check
#get input
nameFirst = input("Please enter your first name: ")
nameLast = input("Please enter your Last name: ")
age = input("Please enter your age: ")

#Create password
firstPart = nameFirst[(len(nameFirst))-1]
secondPart =2017 - int(age)
thirdPart = nameLast[0].upper()
password = (firstPart) + (str(secondPart)) + (thirdPart)

print(password)
