month = (input('Please enter a month: '))
winter = ['december','january','febuarary']
spring = ['march', 'april', 'may']
summer = ['june','july','august']
fall = ['september', 'october','november']

if month.lower() in winter :
    print('It is', month, 'it is winter I suggest snowboarding')
elif month.lower() in spring :
    print('It is', month, 'it is spring I suggest hiking')
elif month.lower() in summer :
    print('It is', month, 'it is summer I suggest swimming')
elif month.lower() in fall :
    print('It is', month, 'it is fall I suggest biking')



num1 = int(input('Please enter a integer: '))
num2 = int(input('Please enter a integer: '))
num3= int(input('Please enter a integer: '))
list = [num1,num2,num3]
#assending
alist = sorted(list, key=int)
print (alist)
#dessending
dlist = sorted(list, key=int, reverse=True)
print(dlist)

