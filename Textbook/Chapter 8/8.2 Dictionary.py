#A container that keeps values with a key word

#creating empty
emptyDict = {}

#creating dictionaries
contacts = { "Fred": 7235591, "Mary": 3841212, "Bob": 3841212, "Sarah": 2213278 }

#duplicating dictionary
oldContacts = dict(contacts)

# can call elements by key
print(contacts["Fred"])

#can use in or not in functions

#can use get method instead
number = contacts.get("Fred", 411)
#The 411 is a return value which is returned if fred is not found in contacts

#adding/modifying
#to add
contacts["John"] = 4578102
#to modify
contacts["John"] = 2228102

#Removing
contacts.pop("John")
#To prevent exceptions
if "Fred" in contacts :
    contacts.pop("Fred")

#Travrsing a dictionary
print("My Contacts:")
for key in contacts :
    print(key)

#Transversing in order
print("My Contacts:")
for key in sorted(contacts) :
    print((key, contacts[key]))

#Iterating dict with more effeciency
for item in contacts.items() :
    print(item[0], item[1])
