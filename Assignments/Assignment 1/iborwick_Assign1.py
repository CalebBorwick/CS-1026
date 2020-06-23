#Ian Borwick Assignement 1
#Coffee or Tea, I See.
#This software will take drink orders for coffee or tea and give a cost based off of the size and flavouring added.
#Input information
nameFirst = str(input('Please enter your first name: '))
#Variables
#Cost Variables
cost = 1.50
# Tea or Coffee. This input determines which root the code will take.
drinkType = input('Would you like coffee or tea: ')

#Coffee. This code is coffee specific and will take your flavour and size and give a cost
if drinkType.lower() == "coffee" or drinkType.lower() == "c" :
    coffeeFlavour = input('Would you like vanilla, chocolate, maple, or none: ').lower().capitalize()
    #Vanilla. This code is specific for coffee and vanilla flavouring using and will take your size and give a cost
    if coffeeFlavour.lower() == "vanilla" or coffeeFlavour.lower() == 'v' :
        cost =(cost+0.25)
        #This code will take your size and give you a final price
        drinkSize = input('Please choose drink size small, medium, or large: ')
        if drinkSize.lower() == 'large' or drinkSize.lower() == 'l' :
            cost = (cost+1.75)
            print('That will be $', round((cost*1.11),2), 'for a large coffee with vanilla for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'medium' or drinkSize.lower() == 'm':
            cost = (cost+1.00)
            print ('That will be $', round((cost*1.11),2), 'for a medium coffee with vanilla for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'small' or drinkSize.lower() == 's' :
            cost = (cost+0.00)
            print('That will be $', round((cost*1.11),2), 'for a small coffee with vanilla for', nameFirst.lower().capitalize())
        #Error statment
        else:
            print('Please enter a valid input')
    #Chocolate. This code is specific for coffee and chocolate flavouring using and will take your size and give a cost
    elif coffeeFlavour.lower() == "chocolate" or coffeeFlavour.lower() == "c" :
        cost = (cost+0.75)
        #This code will take your size and give you a final price
        drinkSize = input('Please choose drink size small, medium, or large: ')
        if drinkSize.lower() == 'large' or drinkSize.lower() == 'l' :
            cost = (cost+1.75)
            print('That will be $', (round((cost*1.11),2)), 'for a large coffee with chocolate for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'medium' or drinkSize.lower() == 'm' :
            cost = (cost+1.00)
            print('That will be $', (round((cost*1.11),2)), 'for a medium coffee with chocolate for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'small' or drinkSize.lower() == 's':
            cost = (cost+0.00)
            print('That will be $', (round((cost*1.11),2)), 'for a small coffee with chocolate for', nameFirst.lower().capitalize())
        #Error statment
        else :
            print('Please enter a valid input')
    #Maple. This code is specific for coffee and maple flavouring using and will take your size and give a cost
    elif coffeeFlavour.lower() == 'maple' or coffeeFlavour.lower() == 'm' :
        cost = (cost+0.50)
        #This code will take your size and give you a final price
        drinkSize = input('Please choose drink size small, medium, or large: ')
        if drinkSize.lower() == 'large' or drinkSize.lower() == 'l' :
            cost = (cost+1.75)
            print('That will be $', (round((cost*1.11),2)), 'for a large coffee with maple for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'medium' or drinkSize.lower() == 'm' :
            cost = (cost+1.00)
            print('That will be $', (round((cost*1.11),2)), 'for a medium coffee with maple for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'small' or drinkSize.lower() == 's' :
            cost = (cost+0.00)
            print('That will be $', (round((cost*1.11),2)), 'for a small coffee with maple for', nameFirst.lower().capitalize())
        #Error statment
        else :
            print('Please enter a valid input')
    #None. This code is specific for coffee and no flavouring using and will take your size and give a cost
    elif coffeeFlavour.lower() == 'none' or coffeeFlavour.lower() == '' :
        cost = (cost + 0.00)
        #This code will take your size and give you a final price
        drinkSize = input('Please choose drink size small, medium, or large: ')
        if drinkSize.lower() == 'large' or drinkSize.lower() == 'l' :
            cost = (cost+1.75)
            print('That will be $', (round((cost*1.11),2)), 'for a large coffee without flavour for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'medium' or drinkSize.lower() == 'm' :
            cost = (cost+1.00)
            print('That will be $', (round((cost*1.11),2)), 'for a medium coffee without flavour for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'small' or drinkSize.lower() == 's' :
            cost = (cost+0.00)
            print('That will be $', (round((cost*1.11),2)), 'for a small coffee without flavour for', nameFirst.lower().capitalize())
        #Error statments
        else :
            print('Please enter a valid input')
    else :
        print ('Please enter a valid input')

#TEA. This code is tea specific and will take your flavour and size and give a cost
elif drinkType.lower() == 'tea' or drinkType.lower() == 't' :
    teaFlavour = input("Would you link to add lemon, mint or none: ")
    #Mint. This code is specific for tea and mint flavouring using and will take your size and give a cost
    if teaFlavour.lower() == 'mint' or teaFlavour.lower() == 'm' :
        cost = (cost + 0.50)
        #This code will take your size and give you a final price
        drinkSize = input('Please choose drink size small, medium, or large: ')
        if drinkSize.lower() == 'large' or drinkSize.lower() == 'l' :
            cost = (cost+1.75)
            print('That will be $', (round((cost*1.11),2)), 'for a large tea with mint for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'medium' or drinkSize.lower() == 'm':
            cost = (cost+1.00)
            print('That will be $', (round((cost*1.11),2)), 'for a medium tea with mint for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'small' or drinkSize.lower() == 's' :
            cost = (cost+0.00)
            print('That will be $', (round((cost*1.11),2)), 'for a small tea with mint for', nameFirst.lower().capitalize())
        #Error statment
        else:
            print('Please enter a valid input')
    #Lemon. This code is specific for tea and lemon flavouring using and will take your size and give a cost
    elif teaFlavour.lower() == 'lemon' or teaFlavour.lower() == 'l' :
        cost = (cost+0.25)
        #This code will take your size and give you a final price
        drinkSize = input('Please choose drink size small, medium, or large: ')
        if drinkSize.lower() == 'large' or drinkSize.lower() == 'l' :
            cost = (cost+1.75)
            print('That will be $', (round((cost*1.11),2)), 'for a large tea with lemon for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'medium' or drinkSize.lower() == 'm' :
            cost = (cost+1.00)
            print('That will be $', (round((cost*1.11),2)), 'for a medium tea with lemon for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'small' or drinkSize.lower() == 's' :
            cost = (cost+0.00)
            print('That will be $', (round((cost*1.11),2)), 'for a small tea with lemon for', nameFirst.lower().capitalize())
        #Error statment
        else :
            print('Please enter a valid input')
    #None. This code is specific for tea and no flavouring using and will take your size and give a cost
    elif teaFlavour.lower() == 'none' or teaFlavour.lower() == '':
        cost = (cost + 0.00)
        #This code will take your size and give you a final price
        drinkSize = input('Please choose drink size small, medium, or large: ')
        if drinkSize.lower() == 'large' or drinkSize.lower() == 'l' :
            cost = (cost+1.75)
            print('That will be $', (round((cost*1.11),2)), 'for a for a large tea without flavouring for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'medium' or drinkSize.lower() == 'm' :
            cost = (cost+1.00)
            print('That will be $', (round((cost*1.11),2)), 'for a medium tea without flavouring for', nameFirst.lower().capitalize())
        elif drinkSize.lower() == 'small' or drinkSize.lower() == 's' :
            costc = (cost+0.00)
            print('That will be $', (round((cost*1.11),2)), 'for a small tea without flavouring for', nameFirst.lower().capitalize())
        #Error statements
        else :
            print('Please enter a valid input')
    else :
        print('Please enter a valid input')
else :
    print ('Please enter a valid input')
