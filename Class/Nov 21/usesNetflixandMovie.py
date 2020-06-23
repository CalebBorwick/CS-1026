from Movie_Class import Movie
from Netflix_Class import Netflix

m1 = Movie("Sinister", 2012)
m1.setGenere("horror")
m1.setGenere(6.3)

m2 = Movie("Shrek", 2001)
m2.setGenere("Animation")
m2.setRating(5)


m3 = Movie("Die Hard", 1993)
m1.addActor("Bruce Willis")
m1.addActor("Ben Afleck")
m1.setGenere(8)

m4 = Movie("Armageddon", 1998)
m4.setGenere("Action")
m4.setRating(3)


na1 = Netflix("Caleb", "Budget")
print(na1.getID())
na1.addFav(m1)
na1.addFav(m2)
na1.addFav(m3)
print(na1.getFav())
print(na1.findMoviesWithHighestRating())
na2 = Netflix("Shawn", "Budget")
