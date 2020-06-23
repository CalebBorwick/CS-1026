#the for loop
i = 3
j =0
n = 0
while i>0 :
    i=i -1
    j = j+1
    n = n+i-j
    print(i,j,n)
#what is the output code (10 midterm questions)

#pulse check sum of values
number = int(input('Enter a number: '))
total = 0
for i in range(0, number,2):
    total = total + i
print(total)

#The while loop
#Sentinal values

#Initialize variables
total = 0.0
count = 0
#Initailize salary to non sentinal value
salary = 0.0

while salary >= 0.0 :
    salary = float(input('Enter a salary or -1 to finish:'))
    if salary >= 0.0 :
        total = total + salary
        count = count + 1
#compute the average salvary
if count > 0 :
    average = total / count
    print('Average salary is: ', average)
else :
    print ("No Data was entered")

#pulse check 2
numberOfGrades = int(input('Enter the number of grades: '))
grades = 0
gradeNumber = 0
while grades < numberOfGrades :
    newGrade = int(input('Enter Grade: '))
    gradeNumber = (gradeNumber + newGrade)
    grades = grades+ 1
average = gradeNumber/numberOfGrades
print(round(average,0),'%')



#loops

#Creathe constants
INITIAL_BALANCE = 10000.00
TARGET = 2 * INITIAL_BALANCE
RATE = 5.0
#INtialize loops and variables
balance = INITIAL_BALANCE
year = 0
#Count years required to double balance
while balance < TARGET :
    year = year + 1
    intrest = balance * RATE / 100
    balance = balance +intrest
#Print results
print('The inverstment will double after', year, 'years')


#pulse check

g1 = input('Enter grade 1: ')
if g1.isdigit():
    g1 = int(g1)
    g2 = input('Enter grade 2: ')
    if g2.isdigit() :
        g2 = int(g2)
        g3 = input('Enter grade 3: ')
        if g3.isdigit() :
            g3 = int(g3)
            g4 = input('Enter grade 4: ')
            if g4.isdigit() :
                g4 = int(g4)
                average = ((g1+g2+g3+g4)/4)
                print('The average is: ', average)
            else :
                print('Invalid Input')
        else :
            print('Invalid Input')
    else :
        print('Invalid Input')
else :
    print('Invalid Input')

