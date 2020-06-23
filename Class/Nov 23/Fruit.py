class Fruit:
    def __init__(self,t,c,w):# Constructor
        self._type = t
        self._color = c
        self._weight = w


    def getType(self):
        return self._type
    def getColor(self):
        return self._color
    def getWeight(self):
        return self._weight

    def setWeight(self,we):
        if isinstance(we,float):
            self._weight = we

    def __repr__(self):
        return "This fruit is a " + self._type +" and it weighs "+ str(self._weight)

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self._type == other._type and self._color == other._color
        return False

    def __add__(self, other):
        if isinstance(other, Fruit):
            if self._type == other._type:
                return ("The new weight is "+str(self._weight+other._weight))
            else:
                return("SMOOTHIE!!!!!!")
        else:
            return -1


f1 = Fruit("Mango","Green",1.34)
f2 = Fruit("Banana", "Yellow", 0.5)
f3 = Fruit("Banana", "Green", 3.5)
f4 = Fruit("Banana", "Green", 3.56566)

print(f1,f2,f3)
if f1==f2:
    print("Fruit 1 and 2 are the same")
if f2==f3:
    print("Fruit 2 and  are the same")
if f3==f4:
    print("Fruit 3 and 4 are the same")

if f3 == "cow":
    print("this shouldnt work")
print(f1+f2)
print(f2+f3)
print(f3+f4)


#list of Fruit
listOfFruit = [f1,f2,f3,f4]
for el in listOfFruit:
    print(el.getType())

x= sorted(listOfFruit, key=Fruit.getWeight)
for el in x:
    print(el)

print(x[0].getWeight())


#Dictionary
f1.setWeight(0.1)
f2.setWeight(23456)

dof= {"fruit1": f1, "fruit2":f2, "fruit3":f3, "fruit4":f4}
for el in dof:
    print(dof[el])

y = sorted(dof.values(), key=Fruit.getWeight, reverse=True)
print(y[0])
