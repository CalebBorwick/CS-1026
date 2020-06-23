from random import random
tries = 10000
hits = 0
for i in range(tries) :
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r
    if x*x+y*y <= 1 :
        hits = hits +1
piEstimate = 4.0 *hits/tries
print("Estamite for pi is", piEstimate)

from random import randint

for i in range(10) :
    d1 = randint (1,6)
    d2 = randint (1,6)
    print(d1,d2)

from random import random
for i in range(10) :
    value = random()
    print(value)
