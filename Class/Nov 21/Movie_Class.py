class Movie:
    def __init__(self, t, y): #accessors were only year and title
        self._title = t
        self._year = y
        self._genre = ""
        self._cast = []
        self._rating = 0

    def getTitle(self):
        return self._title

    def getYear(self):
        return self._year

    def getGenre(self):
        return self._genre

    def getCast(self):
        return self._cast

    def getRating(self):
        return self._rating

    def setGenere(self,g):
        self._genre = g

    def setRating(self,r):
        self._rating = r

    def addActor(self,a):
        if isinstance(a,str):
            self._cast.append(a)


m1 = Movie("Sinister", 2012)
m1.setGenere("horror")
m1.setGenere(6.3)

m2 = Movie("Shrek", 2001)
m2.setGenere("Animation")
m2.setRating(5)

