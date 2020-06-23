# Replace the placeholders and run the Python program

import random
name = input("Please enter your name: ")

for x in range(0,20):
    print("test",x)
    if x % 3 ==0:
        print(name)
    else  :
        print(random.randint(1,10))
