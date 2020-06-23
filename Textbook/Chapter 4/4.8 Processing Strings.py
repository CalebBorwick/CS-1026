

string = input('Enter a phrase: ')
found = False
position = len(string)-1
while not found and position >= 0 :
    if string[position].isdigit :
        found = True
    else :
        position = position - 1


string = input('Enter a phrase: ')
found = False
position = 0
while not found and position < len(string) :
    if string[position].isdigit() :
        found = True
    else :
        position = position +1
if found :
    print("First digit occurs at position", position)
else :
    print ("The string does not contain a digit")

string = input('Enter a phrase: ')
uppercase = 0
for char in string :
    if char.isupper() :
        uppercase = uppercase + 1
print(uppercase)

