#Drink order
wineOrder = input("Enter Y for alcoholic beverage and N for non-alcoholiv beverage: ")
if wineOrder == 'Y' :
    age =input ('Show id with age on it: ')
    if int(age) >= 21 :
        print ('Here is your alcoholic drink')
    else :
        print('You are toooooo young')
else :
    print ('here is your nonalcoholic drink')

#Tax rates

rate1 = 0.10
rate2 = 0.25
rate1_single_limit = 32000.0
rate1_married_limit = 64000.0

#read income and marital status
income = float(input("please input your income: "))
maritalStatus = input("please enter s for single or m for married: ")

#compute taxes due
tax1 = 0.0
tax2 = 0.0

if maritalStatus == "s" :
    if income <= rate1_single_limit :
        tax1 = rate1 * income
    else :
        tax1 = rate1 * rate1_single_limit
        tax2 = rate2 * (income - rate1_single_limit)
else :
    if income <= rate1_married_limit :
        tax1 = rate1 *income
    else :
        tax1 = rate1 * rate1_married_limit
        tax2 = rate2 * (income - rate1_married_limit)
totalTax = tax1 + tax2
print('The tax is $%.2f' % totalTax)
