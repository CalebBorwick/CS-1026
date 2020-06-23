infile = open("test.txt", "r",encoding="utf-8")
keywords = open("keywords.txt","r",)
easternTimeZoneScore = 0.0
easternTimeZoneTweetNum = 0.0
centralTimeZoneScore = 0.0
centralTimeZoneTweetNum = 0.0
mountainTimeZoneScore = 0.0
mountainTimeZoneTweetNum = 0.0
pacificTimeZoneScore = 0.0
pacificTimeZoneTweetNum = 0.0

for line in infile:
    value = line.rstrip()
    fixedTweets = " "
    wordList = value.split()

    keywordsList = []
    numList = []
    for line in keywords:
        stuff = line.split(',')
        key = stuff[0]
        keywordsList.append(key)
        num = stuff[1].strip('/n')
        num = float(num)
        numList.append(num)
    value = 0
    keyNum = 0
    score = 0



    for word in wordList :
        word = word.strip(".,?!:;()!@#[]")
        word = word.lower()
        word = word + " "
        fixedTweets = fixedTweets + word
        fixed = fixedTweets.split()
    latitude = float(fixed[0])
    longitude = float(fixed[1])

    #Finds # of key terms
    for k in keywordsList:
        if k in fixedTweets:
            keyNum = keyNum+ 1
            #Finds the positions of the keyterms and uses that position in the number list to get the corosponding number
            for i, j in enumerate(keywordsList):
                if j == k:
                    value = value + numList[i]
                    score = (value/keyNum)

    #Find proper timezone for each value
        if latitude> 24.660845 and latitude < 49.189787:
            if longitude > -87.518395 and longitude <= -67.444574:
                easternTimeZoneScore = easternTimeZoneScore + score
                easternTimeZoneTweetNum = easternTimeZoneTweetNum +1
            elif longitude >= -101.998892 and longitude < -87.51839:
                centralTimeZoneScore = centralTimeZoneScore + score
                centralTimeZoneTweetNum = centralTimeZoneTweetNum +1
            elif longitude >= -115.236428 and longitude < -101.998892:
                mountainTimeZoneScore = mountainTimeZoneScore + score
                mountainTimeZoneTweetNum = mountainTimeZoneTweetNum +1
            elif longitude >= -125.242264 and longitude < -115.236428:
                pacificTimeZoneScore = pacificTimeZoneScore + score
                pacificTimeZoneTweetNum = pacificTimeZoneTweetNum +1
            else:
                print   ("")
        else:
            print   ("")

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
