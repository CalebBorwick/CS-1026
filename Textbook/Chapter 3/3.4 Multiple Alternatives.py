#email

#pulse check

temp = float(input("what is the tempature:"))
degree = input("Enter C for Celsius or enter F for Fahrenheit: ")

if degree == "F" or "f" :
    temp = (temp - 32) * 5 / 9

if temp >= 100 :
    print('It is', temp, 'outside the water will be gasous')
elif temp >= 0 :
    print('It is', temp, 'outside and the water will be liquid')
elif temp < 0 :
    print('It is', temp,'outside and the water will be solid' )

#Earthquake
richter = float(input('Enter the scale of the earthquake: '))
if richter >= 8.0 :
    print ('Most destructive fall')
elif richter >= 7.0 :
    print("Many buildings destroyed")
elif richter >= 6.0 :
    print('Many buildings damageds few collapsed')
elif richter >= 4.5 :
    print('damage to poorly built buildings')
elif richter :
    print('no destruction of buildings')
