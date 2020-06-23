#example
inputFile = "Mary had a little lamb"
for line in inputFile:
    line = line.rsplit()

    #reading words
#line = line.rstrip()
#wordList = line.split
#word = word.rstrip('.,!?')

#example Lyrics - reading words
inputFile = open('lyrics.txt', 'r')
for line in inputFile:
    line = line.rstrip()
    wordList = line.split()
    for word in wordList:
        word = word.rstrip(",.!?")
        print(word)
inputFile.close()

#Reading charecters
inputFile = open("lyrics.txt", 'r')
char = inputFile.read(1)
while char !="":
    char = inputFile.read(1)
inputFile.close()

#Example
infile = open("country.txt", 'r')
line = infile.readline()
while line != "":
    countryName = line.rstrip()
    line = infile.readline()
    pop = int(line)
    line = infile.readline()
    print(countryName, 'population is', pop)
infile.close

#Pulse check
infile = open('Items.txt','r')
infile.readline()
listOfCost = []
listOfItems = []
for line in infile:
    #print(line)
    stuff = line.rsplit(',',2)
    cost = (stuff[0])
    cost = cost.strip('$')
    cost = cost.replace(',', '')
    cost = float(cost)
    #method chaining - 4 lines above are the same as the one below
    #cost = float(stuff[0].strip('$').replace(',',''))
    listOfCost.append(cost)
    listOfItems.append(int(stuff[2]))


average = sum(listOfCost)/sum(listOfItems)
print(round(average,2))
