#pulse check
def friendGift(amount) :
    if amount < 20 :
        print('slippers')
    elif amount < 50 :
        print('Book')
    else:
        print('Gift card')

def familyGift(amount) :
    if amount < 200 :
        print('headphones')
    elif amount < 1000 :
        print('leather jacket')
    else:
        print('computer')

group = input('Please enter group friend or family: ' )
amount = int(input('Please enter the amount: '))
if group.lower() == "friend" :
    friendGift(amount)
elif group.lower() == 'family' :
    familyGift(amount)
else :
    print('Enter valid input')
