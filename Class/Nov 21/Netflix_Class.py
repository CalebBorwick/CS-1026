from Movie_Class import Movie

class Netflix:
    ID = 1000
    def __init__(self,n,a):
        self._accountType = a
        self._name = n
        self._fav = set()
        Netflix.ID += 1
        self._ID = Netflix.ID

    def getName(self):
        return self._name

    def getID(self):
        return self._ID

    def getFav(self):
        return self._fav

    def getAcountType(self,ac):
        self._accountType = ac

    def addFav(self, show):
        print(show)
        if isinstance(show,Movie):
            self._fav.add(show)
            print(show.getTitle(),"has been added")

    def removeMovie(self,m):
        self._fav.discard(m)

    def findMovieByGenre(self, g):
        listofMovies=[]
        for movie in self._fav:
            if movie.getGenre() == g:
                listofMovies.append(movie.getTitle())
        return listofMovies

    def findMoviesWithHighestRating(self):
        rating = -1
        movieName = ""
        for el in self._fav:
            if el.getRating()> rating:
                rating =el.getRating()
                movieName = el.getTitle()
        return movieName

    def findMoviesWithHighestRating2(self):
        x= sorted(self._fav,key = Movie.getRating(), reverse = True)
        print(x[-1].getTitle(), x[-1].getYear())
        return x[0].getTitle()

    def displayNetflixAccount(self):
        print("*****NETFLIX ACCOUNT*****")
        print("Name:",self.getName())
        print("ID", self._ID)




