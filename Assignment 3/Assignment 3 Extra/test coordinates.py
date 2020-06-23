
easternTimeZoneScore = 0.0
easternTimeZoneTweetNum = 0.0
centralTimeZoneScore = 0.0
centralTimeZoneTweetNum = 0.0
mountainTimeZoneScore = 0.0
mountainTimeZoneTweetNum = 0.0
pacificTimeZoneScore = 0.0
pacificTimeZoneTweetNum = 0.0

def getTimeZone(lat,long):
        lat = lat.rsplit()
        lat[0] = lat[0].strip("[")
        lat[0] = lat[0].strip(",")
        long =long.rsplit()
        long[1] = long[1].strip("]")
        longitude = (long[1])
        latitude = (lat[0])
        latitude = float(latitude)
        longitude = float(longitude)
            #Find proper timezone for each value
        if latitude> 24.660845 and latitude < 49.189787:
            if longitude > -87.518395 and longitude <= -67.444574:
                return  ("Eastern")
            elif longitude >= -101.998892 and longitude< -87.51839:
                return   ("Central")
            elif longitude >= -115.236428 and longitude < -101.998892:
                return   ("Mountain")
            elif longitude >= -125.242264 and longitude < -115.236428:
                return   ("Pacific")
            else:
                return   ("None")
        else:
            return   ("None")


def findValue(tweet):
    keywordsList = []

    for line in tweet:
        value = line.rstrip()
        fixedTweets = " "
        wordList = value.split()
        #striping away special charecters and punctuation and seperating words out
        for word in wordList :
            word = word.strip(".,?!:;()!@#")
            word = word.lower()
            word = word + " "
            fixedTweets = fixedTweets + word
            print(fixedTweets)

        tweetNum = 0
        value = 0
        for line in keywords:
            stuff = line.split(',')
            key = stuff[0]
            num = stuff[1].strip('/n')
            num = float(num)
            if key in fixedTweets:
                print(key)
                value = num + value
                keyNum = keyNum + 1

        try:
            score =  (value/keyNum)
            score = float(score)
            return (score)
        except ZeroDivisionError:
            return (0)


keyfile = input("Please enter keywords file name: ")
try:
    keywords = open(keyfile, 'r',encoding="utf-8")
except FileNotFoundError:
    print("Please eneter a valid filename")
    quit()

infile = input("Please enter a tweet file name: ")
try:
    tweetsFile = open(infile, "r",encoding="utf-8")
except FileNotFoundError:
    print("Please enter a valid filename")
    quit()

allTweets= tweetsFile.read().split("/n")

for line in allTweets:
    score = findValue(line)
    timeZone = getTimeZone(line,line)
    if timeZone == "Eastern":
        easternTimeZoneScore = easternTimeZoneScore + score
        easternTimeZoneTweetNum = easternTimeZoneTweetNum +1
    elif timeZone == "Central":
        centralTimeZoneScore = centralTimeZoneScore + score
        centralTimeZoneTweetNum = centralTimeZoneTweetNum +1
    elif timeZone == "Mountain":
        mountainTimeZoneScore = centralTimeZoneScore +score
        mountainTimeZoneTweetNum = mountainTimeZoneTweetNum +1
    elif timeZone == "Pacific":
        pacificTimeZoneScore = pacificTimeZoneScore + score
        pacificTimeZoneTweetNum = pacificTimeZoneTweetNum +1


try:
    print ("There were", int(easternTimeZoneTweetNum),"tweets from the Eastern Time Zone. Its happiness score is",
            round(easternTimeZoneScore/easternTimeZoneTweetNum,2))
except ZeroDivisionError:
    print("east 0")
try:
    print ("There were", int(centralTimeZoneTweetNum),"tweets from the Central Time Zone. Its happiness score is",
            round(centralTimeZoneScore/centralTimeZoneTweetNum,2))
except ZeroDivisionError:
    print("central 0")
try:
    print ("There were", int(mountainTimeZoneTweetNum),"tweets from the Mountain Time Zone. Its happiness score is",
            round(mountainTimeZoneScore/mountainTimeZoneTweetNum,2))
except ZeroDivisionError:
    print("mountain 0")

try:
    print ("There were", int(pacificTimeZoneTweetNum),"tweets from the Pacific Time Zone. Its happiness score is",
            round(pacificTimeZoneScore/pacificTimeZoneTweetNum,2))
except ZeroDivisionError:
    print("pacific 0")
