#boolean variables in sentinel values
done = False
while not done :
    value = float(input('Enter a salary or negative to end: '))
    if value >= 0 :
        done = True
    else :
        print(value)

#initilize Variables to maintain running total and count
total = 0.0
count = 0
#initilize values to any non sentinal values
salary = 0.0
while salary >= 0.0 :
    salary = float(input('Please enter your salary or a negative number to end: '))
    if salary >= 0.0 :
        total = salary + total
        count = count+1
#compute the average salary
if count >=0 :
    average = total/count
    print('The average salary is', round(average,2))
else :
    print('No data entered')
