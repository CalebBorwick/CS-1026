#Ian Borwick 2509408446
#Class - CountryCalalogue Class

#Import Country Class
from country import Country

#Global Lists and dictionaries
countryCat = []
cDictionary = {}

#Class setter
class CountryCatalogue:
    #Constructor taking information from provided data sets
    #Strips and prepares information for proper use converting it to proper class
    def __init__(self,cn,ci):
        data = open(ci,"r")
        continents = open(cn, "r")
        continents.readline()
        for line in continents:
            splitted = line.split(",")
            country = splitted[0]
            continent= splitted[1].rstrip()
            cDictionary[country] = continent
        data.readline()
        for line in data:
            fixed = line.split("|")
            fixed[2] = fixed[2].rstrip()
            fixed[1] = fixed[1].replace(",","")
            fixed[2] = fixed[2].replace(",","")
            if fixed[0] in cDictionary:
                cnt = (cDictionary[fixed[0]])
                fixed[0] = str(fixed[0])
                fixed[1] = int(fixed[1])
                fixed[2] = float(fixed[2])
                cnt = str(cnt)
                self._name = fixed[0]
                self._population = fixed[1]
                self._area = fixed[2]
                self._continent = cnt
                info = Country(fixed[0],fixed[1],fixed[2],cnt)
                if isinstance(info,Country):
                    countryCat.append(info)

    #Finds country and returns country object
    #Uses Country Class in order to get information
    #Checks if it is a in data set
    def findCountry(self,name):
        if name in cDictionary:
            for el in countryCat:
                if name == (el.getName()):
                    return (el)
        else:
            return None

    #Sets population of a country to allow for change
    #Uses the Country class in order to change population
    #Checks if it is a in data set
    def setPopulationOfCountry(self,name,pop):
        if name in cDictionary:
            if isinstance(pop,int):
                for el in countryCat:
                    if name == (el.getName()):
                        el.setPopulation(pop)
                        return True

    #Sets area of a country to allow for change
    #Uses the Country class in order to change area
    #Checks if it is a in data set
    def setAreaOfCountry(self,name, ar):
        if name in cDictionary:
            if isinstance(ar,float):
                for el in countryCat:
                    if name == (el.getName()):
                        (el.setArea(ar))
                        return True

    #Allows your new countries to be added to data set
    #Checks if it is in data set to prevent duplication
    def addCountry(self,name,pop,area,continent):
        if name != cDictionary:
            cDictionary[name] = continent
            countryCat.append(Country(name,pop,area,continent))
            print(name,"successfully added to data base")
            return True
        else:
            return False
    #Allows for the removeal of data set if data is in set already
    def deleteCountry(self,name):
        if name in cDictionary:
            cDictionary.pop(name)
            for el in countryCat:
                if name == (el.getName()):
                    position = countryCat.index(el)
                    countryCat.pop(position)
                    print(name, "has been removed")

            
    #Prints the country cataloug
    def printCountryCatalogue(self):
        print("Country|Population|Area|Continent")
        for el in countryCat:
            print(el.getName(),"|",el.getPopulation(),"|",el.getArea(),"|",el.getContinent(), sep="")

    #Finds Countries in data set by continent
    def getCountriesByContinent(self,continent):
        listByContinent= []
        for el in countryCat:
            if self == (el.getContinent()):
                listByContinent.append(el.getName())
        return listByContinent
    
    #Finds Countries in data set by population from highest to lowest for a specific continent
    def getCountriesByPopulation(self, continent):
        listByPop = []
        for el in countryCat:
            if self == (el.getContinent()):
                add = (el.getName(),el.getPopulation())
                listByPop.append(add)
            elif self == (""):
                add = (el.getName(),el.getPopulation())
                listByPop.append(add)
        sortedByPop = sorted(listByPop, key=lambda tup:-tup[1])
        return sortedByPop

    #Finds Countries in data set by area from highest to lowest for a specific continent
    def getCountriesByArea(self,continent):
        listByArea = []
        for el in countryCat:
            if self == (el.getContinent()):
                add = (el.getName(),el.getArea())
                listByArea.append(add)
            elif self == (""):
                add = (el.getName(),el.getArea())
                listByArea.append(add)
        sortedByArea = sorted(listByArea, key=lambda tup:-tup[1])
        return sortedByArea

    #Finds the most populated continent
    #Finds the total population for contenet
    #Returns continent with largest poulation
    def findMostPopulousContinent(self):
        continentList = {}
        numbers = []
        asiaNum= 0.0
        southamericaNum = 0.0
        northAmericaNum = 0.0
        africaNum = 0.0
        europeNum = 0.0
        austrialiaNum = 0.0
        antarcticaNum = 0.0
        for el in countryCat:
            if el.getContinent() == "Asia":
                asiaNum = asiaNum + el.getPopulation()
            elif el.getContinent() == "South America":
                southamericaNum = southamericaNum + el.getPopulation()
            elif el.getContinent() == "North America":
                northAmericaNum = northAmericaNum +el.getPopulation()
            elif el.getContinent() == "Africa":
                africaNum = africaNum + el.getPopulation()
            elif el.getContinent() == "Europe":
                europeNum = europeNum + el.getPopulation()
        continentList["Asia"] = asiaNum
        continentList["South America"] =southamericaNum
        continentList["North America"] =northAmericaNum
        continentList["Africa"] =africaNum
        continentList["Europe"] =europeNum
        continentList = sorted(continentList, key=continentList.get, reverse=True)
        continent = continentList[0]
        numbers.append(asiaNum)
        numbers.append(southamericaNum)
        numbers.append(northAmericaNum)
        numbers.append(africaNum)
        numbers.append(europeNum)
        numbers = sorted(numbers,key=int, reverse=True)
        biggestpop = numbers[0]
        returnValue= continent,biggestpop
        return returnValue


    #Finds countries within preset population standards
    #Finds information in data base and uses the Country class to determine population density
    def filterCountriesByPopDensity(self,low,high):
        countryList = []
        for el in countryCat:
            if el.getPopDenisty() <= high and el.getPopDenisty() >= low:
                add = el.getName(), el.getPopDenisty()
                countryList.append(add)
        countryList = sorted(countryList, key=lambda x: x[1], reverse=True)
        return countryList

    #Writes data in speicfic format to another document
    #Sorts the list into alphabetical order
    #Then prepares information for proper format
    def saveCountryCatalogue(self,fname):
        file=open(fname,'w')
        alphaOrder = []
        file.write('Name|Continent|Population|AreaSize|PopulationDensity\n')
        num = 1
        for el in countryCat:
            name =el.getName()
            coninent = el.getContinent()
            pop = el.getPopulation()
            area =el.getArea()
            popDensity = el.getPopDenisty()
            add = ("name","|","continent","|",pop,"|",area,"|",popDensity)
            add= str(add)
            add= "".join(add)
            add = add.replace(" ","")
            add = add.replace("name",name)
            add = add.replace("continent",coninent)
            add = add.replace(",", "")
            add = add.replace("'","")
            add = add.replace("(","")
            add = add.replace(")","")
            alphaOrder.append(add)
        alphaOrder.sort()
        for el in alphaOrder:
            file.write(el+"\n")
            num = num+1
        file.close()
        if num >= 1:
            return num
        else:
            return -1


