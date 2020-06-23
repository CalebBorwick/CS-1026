#Create constant variables
RATE = 5.0
INITIAL_BALANCE =10000.0
TARGET = (2*INITIAL_BALANCE)
#Initialize variables used with the loop
balance = INITIAL_BALANCE
year = 0
#count the years required for the investment to double
while balance < TARGET :
    year = (year+1)
    intrest = ((balance*RATE)/100)
    balance = balance +intrest
#Print the results
print('The investment doubled after', year, 'years.')

counter = 1
while counter <=10 :
    print (counter)
    counter = counter+1

