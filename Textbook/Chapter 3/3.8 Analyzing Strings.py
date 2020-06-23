#substrings
theString = input("Enter a string: ")
theSubstring = input("Enter a substring: ")

if theSubstring in theString :
    print ("The string does contain the substring")

    howMany = theString.count(theSubstring)
    print("It contains", howMany, "instances.")

    where = theString.find(theSubstring)
    print("The first occurence starts at position", where)

    if theString.startswith(theSubstring) :
        print("The string starts with the substring.")
    else:
        print('The string does not start with the substring')

    if theString.endswith(theSubstring) :
        print("The string ends with the substring")
    else:
        print("The string does not end with the substring")
else:
    print("The string does not contain the substring")

#pg 127
#test for charecters
line = "Four score and seven years ago"
if line.islower() :
    print ("The string only contains lowercase letters")
else :
    print("The string contains uppercase and lower case letters")

if line.isalpha() :
    print("The string is valid")
else :
    print("The string must contain only upper and lowercase letters and no special charecters.")
