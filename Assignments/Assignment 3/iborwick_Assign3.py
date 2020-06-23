#Ian Borwick 250950449 - Sentiment Value - Assignment 3
#Main Function

def main():

    #Lists of timezone values and lists for the functions
    easternTimeZoneScore = 0.0
    easternTimeZoneTweetNum = 0.0
    centralTimeZoneScore = 0.0
    centralTimeZoneTweetNum = 0.0
    mountainTimeZoneScore = 0.0
    mountainTimeZoneTweetNum = 0.0
    pacificTimeZoneScore = 0.0
    pacificTimeZoneTweetNum = 0.0
    keywordsList = []
    numList = []
    initialScore = 0
    keyNum = 0
    score = 0
    done = False

    #Opening Files
    #Proper input with read statements and error statments
    tweets = input("Please enter a tweet file name: ")
    try:
        infile = open(tweets, "r",encoding="utf-8")
    except FileNotFoundError:
        print("Please eneter a valid filename")
        quit()

    #Opening the keywords text file with exceptions statement for improper input
    keyfile = input("Please enter a keyword file name: ")
    try:
        keywords = open(keyfile,"r",)
    except FileNotFoundError:
        print("Please enter a valid filename")
        quit()

    #Loop to run through all tweets
    for line in infile:
        value = line.rstrip()
        fixedTweets = " "
        wordList = value.split()

        #Preping keywords to be split into proper lists for later use
        for line in keywords:
            stuff = line.split(',')
            key = stuff[0]
            keywordsList.append(key)
            num = stuff[1].strip('/n')
            num = float(num)
            numList.append(num)

        #Striping away special charecters and punctuation and seperating words out
        for word in wordList :
            word = word.strip(".,?!:;()!@#[]&")
            word = word.lower()
            word = word + " "
            fixedTweets = fixedTweets + word
            fixed = fixedTweets.split()
        #Isolating the Longitude and Latitude for proper region sorting
        latitude = float(fixed[0])
        longitude = float(fixed[1])

        #Finds # of key terms
        for k in keywordsList:
            for s in fixed:
                if s ==k:
                    done = True
                    keyNum = keyNum+ 1
                #Finds the positions of the keyterms and uses that position in the number list to get the corosponding number
                    for i, j in enumerate(keywordsList):
                        if j == k:
                            initialScore = initialScore + numList[i]
                            score = (initialScore/keyNum)



        #TimeZone
        #Checks to see if the tweet is in regions selected as well as adds score and number to tweets to proper time zone
        #statement to make sure tweet had key words
        if done != False:
            if latitude> 24.660845 and latitude < 49.189787:
                if longitude > -87.518395 and longitude < -67.444574:
                    easternTimeZoneScore = easternTimeZoneScore + score
                    easternTimeZoneTweetNum = easternTimeZoneTweetNum +1
                    done = False
                elif longitude > -101.998892 and longitude < -87.51839:
                    centralTimeZoneScore = centralTimeZoneScore + score
                    centralTimeZoneTweetNum = centralTimeZoneTweetNum +1
                    done = False
                elif longitude > -115.236428 and longitude < -101.998892:
                    mountainTimeZoneScore = mountainTimeZoneScore + score
                    mountainTimeZoneTweetNum = mountainTimeZoneTweetNum +1
                    done = False
                elif longitude > -125.242264 and longitude < -115.236428:
                    pacificTimeZoneScore = pacificTimeZoneScore + score
                    pacificTimeZoneTweetNum = pacificTimeZoneTweetNum +1
                    done = False





    #Print statements
    #Try and error statments to prevent zero division error
    try:
        print ("There were", int(easternTimeZoneTweetNum),"tweets from the Eastern Time Zone. Its happiness score is",
                round(easternTimeZoneScore/easternTimeZoneTweetNum,2))
    except ZeroDivisionError:

        print ("There were 0 tweets from the Eastern Time Zone. Its happiness score is 0 ")
    try:
        print ("There were", int(centralTimeZoneTweetNum),"tweets from the Central Time Zone. Its happiness score is",
                round(centralTimeZoneScore/centralTimeZoneTweetNum,2))
    except ZeroDivisionError:
        print("There were 0 tweets from the Central Time Zone. Its happiness score is 0 ")
    try:
        print ("There were", int(mountainTimeZoneTweetNum),"tweets from the Mountain Time Zone. Its happiness score is",
                round(mountainTimeZoneScore/mountainTimeZoneTweetNum,2))
    except ZeroDivisionError:
        print ("There were 0 tweets from the Mountain Time Zone. Its happiness score is 0")
    try:
        print ("There were", int(pacificTimeZoneTweetNum),"tweets from the Pacific Time Zone. Its happiness score is",
                round(pacificTimeZoneScore/pacificTimeZoneTweetNum,2))
    except ZeroDivisionError:
        print("There were 0 tweets from the Pacific Time Zone. Its happiness score is 0")

main()



