infile = open("tweets.txt","r",encoding="utf-8")
keywords = open("keywords.txt","r",encoding="utf-8")
easternTimeZoneScore = 0.0
easternTimeZoneTweetNum = 0.0
centralTimeZoneScore = 0.0
centralTimeZoneTweetNum = 0.0
mountainTimeZoneScore = 0.0
mountainTimeZoneTweetNum = 0.0
pacificTimeZoneScore = 0.0
pacificTimeZoneTweetNum = 0.0
tweetValue = 0


for line in infile:
        value = line.rstrip()
        fixedTweets = " "
        wordList = value.split()
        #striping away special charecters and punctuation and seperating words out
        for word in wordList :
            word = word.strip(".,?!:;()!@#")
            word = word.lower()
            word = word + " "
            fixedTweets = fixedTweets + word
            fixed = fixedTweets.split()

            #Isolating the Longitude and Latitude for proper region sorting
            lat = (line.split(" ",1)[0])
            long= (line.split(" ",2)[1])
            lat = lat.split("[,")
            long = long.strip("]")
            lat= float(lat)
            long = float(long)

                #Find proper timezone for each value
        if lat> 24.660845 and lat < 49.189787:
            if long > -87.518395 and long <= -67.444574:
                timeZone =  ("Eastern")
                easternTimeZoneTweetNum = easternTimeZoneTweetNum + 1
            elif long >= -101.998892 and long< -87.51839:
                timeZone =  ("Central")
                centralTimeZoneTweetNum = centralTimeZoneTweetNum +1
            elif long >= -115.236428 and long < -101.998892:
                timeZone =  ("Mountain")
                mountainTimeZoneTweetNum=mountainTimeZoneTweetNum+1
            elif long >= -125.242264 and long < -115.236428:
                timeZone =  ("Pacific")
                pacificTimeZoneTweetNum = pacificTimeZoneTweetNum +1

            else:
                timeZone =  ("None")
        else:
            timeZone =  ("None")

        keywordNum = 0
        initailScore = 0
        #preps Keywords for proper searching and assigns score to proper time zone
        for phrase in keywords:
            stuff = phrase.split(',')
            key = stuff[0]
            num = stuff[1].strip('/n')
            num = float(num)
        if key in fixedTweets:
            print(key)
            keywordNum = keywordNum +1
            initailScore = initailScore + num
            tweetValue= initailScore/keywordNum

    #Determines specific timezone score
        if timeZone == "Eastern":
            easternTimeZoneScore = easternTimeZoneScore + tweetValue
        elif timeZone == "Central":
            centralTimeZoneScore = centralTimeZoneScore + tweetValue
        elif timeZone == "Mountain":
            mountainTimeZoneScore = centralTimeZoneScore +tweetValue
        elif timeZone == "Pacific":
            pacificTimeZoneScore = pacificTimeZoneScore + tweetValue


print("number of eastern tweets is", easternTimeZoneTweetNum, "the the score is", round((easternTimeZoneScore/easternTimeZoneTweetNum),3))
print("number of central tweets is", centralTimeZoneTweetNum, "the the score is", round((centralTimeZoneScore/centralTimeZoneTweetNum),3))
print("number of mountain tweets is", mountainTimeZoneTweetNum, "the the score is", round((mountainTimeZoneScore/mountainTimeZoneTweetNum),3))
print("number of pacific tweets is", pacificTimeZoneTweetNum, "the the score is", round((pacificTimeZoneScore/pacificTimeZoneTweetNum),3))
