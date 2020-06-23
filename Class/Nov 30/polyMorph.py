class Person:
    def buyGift(self):
        value = int(input("Enter money to spend: "))
        if value < 10:
            print("you are too cheap ")
        elif  10 < = value <= 100:
            print("Het them a gift card")
        elif value< 100:
            print("Get them something fancy")
    def __init__(self,n,y):
        self._name = n
        self._yearOfBirth = y
        self._nationality = ""

    def setNationality(self,na):
        self._nationality = na

    def getName(self):
        return self._name

    def __repr__(self):
        return (self._name + " is "+str(2017-self._yearOfBirth) +" years old")

class Student(Person):
    def __init__(self):

    def __repr__(self):
        return

class Instructor(Person):
    def buyGift(self):
        value = int(input("Enter value: "))
        if value < 10:
            print("you are too cheap ")
        elif  10 < = value <= 100 :
            print("Get them a calculator")
        elif value< 100:
            print("Get them all the books")

    def __init__(self,n,y,s,f):
        self._name= n
        self._yearOfBirth = y
        self._salary = s
        self._facuilty = f
        self._courses = []

    def addCourse(self,course):
        if course not in self._courses:
            self._courses.append(course)

    def setNationality(self,na):
        self._nationality = na

    def getName(self):
        return self._name

    def __repr__(self):
        return self._name+" is " +str(2017-self._yearOfBirth)+ " and teaches in the facuilty of "+ self._facuilty



p1 = Person("Gaston", 1969)
p2 = Person("Paul Walker", 1980, "Geology")
p3 = Instructor("Albert Einstein", 1908, 1000000, "Physics")

listOfPeople = [p1,p2,p3]
for person in listOfPeople:
    print(Person)
