x = float(input("Enter a number (such as 35 or 4.5): "))
y = float(input("Enter a second number: "))

if x==y :
    print ("They are the same")
else :
    if x > y :
        print ("The first number is larger")
    else :
        print("The first number is smaller")
    if -0.01 < x - y and x - y < 0.01 :
        print ("The numbers are close together")
    if x==y + 1 or x==y -1 :
        print("The numbers are one apart")
    if x>0 and y>0 or x<0 and y<0 :
        print("The numbers have the same sign")
    else :
        print("The numbers have differnt signs")
