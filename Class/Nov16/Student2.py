class Student2:
    def __init__(self, n):
        self._name = n
        self._scores = []

    def getName(self):
        return self._name

    def addScore(self, currentScore):
        self._scores.append(currentScore)

    def getAverageScore(self):
        return sum(self._scores)/len(self._scores)

    def getCountOfQuizzes(self):
        return len(self._scores)
