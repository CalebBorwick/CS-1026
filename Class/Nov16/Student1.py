class Student1:
    def __init__(self, n):
        self._name = n
        self._score = 0
        self._numOfQuizzes = 0

    def getName(self):
        return self._name

    def addScore(self, currentScore):
        self._score = self._score + currentScore
        self._numOfQuizzes += 1

    def getAverageScore(self):
        return self._score/self._numOfQuizzes

    def getCountOfQuizzes(self):
        return self._numOfQuizzes
