#Ian Borwick 250950449
#Country Class

#Class setter
class Country:
    #Constructor
    def __init__(self,name,pop,area,contenent):
        self._name = name
        self._population = pop
        self._area = area
        self._continent = contenent

    #Returns Country name
    def getName(self):
        if isinstance(self._name, str):
            return self._name
    #Returns Country population
    def getPopulation(self):
        if isinstance(self._population, int):
            return self._population

    #Returns Country area
    def getArea(self):
        if isinstance(self._area,float):
            return self._area

    #Returns Country's continent
    def getContinent(self):
        if isinstance(self._continent, str):
            return self._continent

    #Sets population of country
    def setPopulation(self,p):
        self._population = p

    #Sets area of country
    def setArea(self,a):
        self._area = a

    #Sets continent of a country
    def setContinent(self,c):
        self._continent = c

    #Calculates and finds population density
    def getPopDenisty(self):
        try:
            popD = round((self._population/self._area),2)
            return popD
        except ZeroDivisionError:
            popD = 0.00

    #Returns class object
    def __repr__(self):
        return self._name +"(population: " + str(self._population) + " size: " +str(self._area) + ") in "+ self._continent


