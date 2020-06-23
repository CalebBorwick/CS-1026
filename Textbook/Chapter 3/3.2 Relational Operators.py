#Relational Operators pg 98
a = 13.999999996
b = round(a,2)
print (b)

#compute discount
originalPrice = float(input("Orignial price before discount: "))
if originalPrice < 128 :
    discountRate = 0.92
else :
    discountRate = 0.82
discountedPrice = discountRate * originalPrice
print('Discounted price: %.2f' % discountedPrice)

# Comparing Intagers
from math import sqrt
m = 2
n = 4
if m * m == n :
    print ('2 times 2 is four')

# Comparing floating-point numbers
x = sqrt(2)
y = 2.0
if x * x == y :
    print ('sqrt(2) times sqrt(2) is 2')
else :
    print ('sprt(2) times sqrt(2) is not two but %.18f' % (x*x))
EPSILON = 1E-14
if abs(x * x - y) < EPSILON :
    print ('sqrt(2) times sqrt(2) is approximatley 2')

#Comparing Strings
s = '120'
t = '20'
if s == t :
    comparison = "is the same as"
else :
    comparison = 'is not the same as'
print ("The string '%s' %s the string '%s'." % (s, comparison, t))

u = "1" + t
if s != u :
    comparison = "not"
else:
    comparison = ""
print("the string '%s' and '%s' are %sidentical." % (s, u, comparison))
