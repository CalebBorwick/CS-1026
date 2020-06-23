#Class Student example
class Student():
    def __init__(self,name):
        self._name = name
        self._score = 0
        self._num_quizzes = 0

    def getName(self):
        return self._name

    def addQuiz(self,score):
        self._score = self._score +score
        self._num_quizzes = self._num_quizzes +1

    def getTotalScore(self):
        return self._score

    def getAverageScore(self):
        return self._score/self._num_quizzes

Stu1 = Student("Kemi")
Stu1.addQuiz(67)
Stu1.addQuiz(100)
Stu1.addQuiz(45)
print("the avergae score of", Stu1.getName(),"is", round(Stu1.getAverageScore(),2))


#Profile
class Profile():
    def __init__(self,i,n,a,c):
        self._id = i
        self._name = n
        self._age = a
        self._city = c
        self._relationshipStatus = "Its Complicated"
        self._profileStatus = "Today is a good day"
        self._friendsList = []

    def __repr__(self):
        return self._name + "has", str(len(self._friendsList))+ "lives in", self._city

    def getRStatus(self, newStat):
        return self._relationshipStatus

    def getPStatus(self):
        return self._profileStatus

    def like(self,otherProfile):
        if otherProfile in self._friendsList:
            return True
        else:
            return False

    def addFriend(self, pta):
        self._friendsList.append(pta)

    def getName(self):
        return self._name


    def printWall(self):
        print(self._name)
        for friend in self. _friendsList:
            print(friend.getName() + friend.getPstatus())

fb1 = Profile(12343, "Kemi Ola", 45, "London")
fb1.getRStatus("Very sad right now but Ill pull through")
fb2 = Profile(2345567, "Matt", 345, "new World")
fb3 = Profile(2345568, "Nick", 45, "Denmark")
fb4 = Profile(2345569, "Sarah", 25, "Japan")
fb1.addFriend(fb2)

print(fb1.like(fb4))
print(fb1.like(fb2))
