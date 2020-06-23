#Ian Borwick 250950449 - Sentiment Value - Assignment 3
#Main Function
def main():

    #Lists of timezone and lists for the functions
    easternTimeZoneScore = 0.0
    easternTimeZoneTweetNum = 0.0
    centralTimeZoneScore = 0.0
    centralTimeZoneTweetNum = 0.0
    mountainTimeZoneScore = 0.0
    mountainTimeZoneTweetNum = 0.0
    pacificTimeZoneScore = 0.0
    pacificTimeZoneTweetNum = 0.0
    tweetValue = 0
    initailScore = 0

    #opening files
    #opening the tweet file with exceptions statement for improper input
    infile = input("Please enter a tweet file name: ")
    try:
        tweetsFile = open(infile, "r")
    except FileNotFoundError:
        print("Please enter a valid filename")
        quit()
    #Opening the keywords text file with exceptions statement for improper input
    keyfile = input("Please enter keywords file name: ")
    try:
        keywords = open(keyfile, 'r')
    except FileNotFoundError:
        print("Please eneter a valid filename")
        quit()

#preps Keywords for proper searching
    for phrase in keywords:
        stuff = phrase.split(',')
        key = stuff[0]
        num = stuff[1].strip('/n')
        num = float(num)

    #Stripping information and caluclating values to be used with the functions to determine which region the score goes to
    for line in tweetsFile:
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
            #finds corosponding score for time zone
            if key in fixed:
                print("yes")
                initailScore = initailScore + num
                tweetValue= initailScore

            #Isolating the Longitude and Latitude for proper region sorting
            lat = (line.split(" ",1)[0])
            long= (line.split(" ",2)[1])
            lat = lat.strip("[,")
            long = long.strip("]")
            lat= float(lat)
            long = float(long)

        #Find proper timezone for each value
        #Checks to see if the tweet is in regions selected
            if lat>= 24.660845 and lat <= 49.189787:
                    if long >= -87.518395 and long <= -67.444574:
                        timeZone =  ("Eastern")
                    elif long >= -101.998892 and long<= -87.51839:
                        timeZone =  ("Central")
                    elif long >= -115.236428 and long < -101.998892:
                        timeZone =  ("Mountain")
                    elif long >= -125.242264 and long < -115.236428:
                        timeZone =  ("Pacific")
                    else:
                        timeZone =  ("None")
            else:
                timeZone =  ("None")

        #Determines specific timezones number of tweets
        if timeZone == "Eastern":
            easternTimeZoneTweetNum = easternTimeZoneTweetNum + 1
        elif timeZone == "Central":
            centralTimeZoneTweetNum = centralTimeZoneTweetNum +1
        elif timeZone == "Mountain":
            mountainTimeZoneTweetNum=mountainTimeZoneTweetNum+1
        elif timeZone == "Pacific":
            pacificTimeZoneTweetNum = pacificTimeZoneTweetNum +1
        #Determines specific timezone score
        if timeZone == "Eastern":
            easternTimeZoneScore = easternTimeZoneScore + tweetValue
        elif timeZone == "Central":
            centralTimeZoneScore = centralTimeZoneScore + tweetValue
        elif timeZone == "Mountain":
            mountainTimeZoneScore = centralTimeZoneScore +tweetValue
        elif timeZone == "Pacific":
            pacificTimeZoneScore = pacificTimeZoneScore + tweetValue






    #Eastern Time Zone Final output prep and print statement
    try:
        easternTimeZoneFinalScore = easternTimeZoneScore/easternTimeZoneTweetNum
        easternTimeZoneFinalScore = round(easternTimeZoneFinalScore,2)
        print("There was", int(easternTimeZoneTweetNum), "tweets with an average happyness score of", int(easternTimeZoneFinalScore), "in the Eastern time zone")
    except ZeroDivisionError:
        print("Error: Division by zero")

    #Eastern Time Zone Final output prep and print statement
    try:
        centralTimeZoneFinalScore = centralTimeZoneScore/centralTimeZoneTweetNum
        centralTimeZoneFinalScore = round(centralTimeZoneFinalScore,2)
        print("There was", int(centralTimeZoneTweetNum), "tweets with an average happyness score of", int(centralTimeZoneFinalScore), "in the Central time zone")
    except ZeroDivisionError:
        print("Error: Division by zero")

    #Mountain Time Zone Final output prep and print statement
    try:
        mountainTimeZoneFinalScore = mountainTimeZoneScore/mountainTimeZoneTweetNum
        mountainTimeZoneFinalScore=round(mountainTimeZoneFinalScore,2)
        print("There was", int(mountainTimeZoneTweetNum), "tweets with an average happyness score of",int(mountainTimeZoneFinalScore), "in the Mountain time zone")
    except ZeroDivisionError:
        print("Error: Division by zero")

    #Pacific Time Zone Final output prep and print statement
    try:
        pacificTimeZoneFinalScore = pacificTimeZoneScore/pacificTimeZoneTweetNum
        pacificTimeZoneFinalScore=round(pacificTimeZoneFinalScore,2)
        print("There was", int(pacificTimeZoneTweetNum), "tweets with an average happyness score of",int(pacificTimeZoneFinalScore), "in the Pacific time zone")
    except ZeroDivisionError:
        print("Error: Division by zero")

main()
