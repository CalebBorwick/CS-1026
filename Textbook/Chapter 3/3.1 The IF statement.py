#The IF statement
actualFloor = 0
floor = int(input ('Enter floor number: '))
if floor > 13 :
    actualFloor = floor - 1
else:
    actualFloor=floor
print ('The elevator will stop on', actualFloor)

#Example 2
totalSales = float(input('Please enter transaction price: '))
if totalSales > 100.0 :
    discount = totalSales * 0.05
    totalSales = totalSales - discount
    print ('You shall recieve a discount of', '%.2f' % discount)
else :
    diff = 100.0 - totalSales
    if diff < 10.0 :
        print ('If you were to purchase our item of the day you can recieve a 5% discount.')
    else :
        print ("You need to spend $", diff, 'more to reieve a 5% discount.')
