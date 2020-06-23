#While verson
stateName = 'Virginina'
i = 0
while i < len(stateName) :
    letter = stateName[i]
    print(letter)
    i = i + 1
#for verson
stateName = 'Virginina'
for letter in stateName :
    print (letter)

#define constants
rate = 5.0
initialBalance = 10000.0
#obtain years for computation
numYears = int(input('Enter number of years: '))
#print the table of balances for each year
balance = initialBalance
for year in range(1,numYears +1) :
    intrest = balance * rate / 100
    balance = balance + intrest
    print ("%4d %10.2f" % (year, balance))
