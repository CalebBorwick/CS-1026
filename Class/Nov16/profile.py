class Profile:
    def __init__(self, i, n, a, c):
        FBID = FBID + 1
        self._id = i = "P" +str(Profile._lastFBID)
        self._name = n
        self._age = a
        self._city = c
        self._relationshipStatus = "IT'S COMPLICATED :|"
        self._profileStatus = "Today is a good day #WESTERN ROCKS"
        self._friendsList = []

    def __repr__(self):
        return self._name + ' has ' +str(len(self._friendsList)) + " friends and lives in "+self._city

    def setRStatus(self, newStat):
        self._relationshipStatus = newStat

    def setPStatus(self, pStat):
        self._profileStatus = pStat

    def getRStatus(self):
        return self._relationshipStatus

    def getPStatus(self):
        return self._profileStatus

    def addFriend(self, pta):
        if isinstance(pta,Profile):
            self._friendsList.append(pta)
            print(pta.getName(), "is now your friend")

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def showWall(self):
        print('*********************', self._name, 'WALL ****************************')
        for friend in self._friendsList:
            print(friend.getName()+ " is saying " + friend.getPStatus())
        print('**********************************************************************')




fb1 = Profile(333, 'John Smith', 566, 'Place in World')
print(fb1.getRStatus())
fb1.setRStatus('VERY SAD RIGHT NOW I LOST MY GIRL :( ')
print(fb1.getRStatus())

fb2 = Profile(23443, 'Pocahontas', 345, 'New world')
fb3 = Profile(3444, 'Tarzan', 344, 'Jungle')
fb4 = Profile(3444, 'Jane', 44, 'Jungle')
fb4.setPStatus('I am in the jungle so so scared')

fb1.addFriend(fb4)
fb1.addFriend(fb3)
print(fb1)

fb1.showWall()
