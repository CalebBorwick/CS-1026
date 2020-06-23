infile = open('keywords.txt', 'r')
tweet = input('Enter a tweet: ')
hWords = []
nWords = []
sWords = []
value = 0
for line in infile:
    stuff = line.split(',')
    word = stuff[0]
    num = stuff[1].strip('/n')
    num = float(num)
    if word in tweet :
        value += num
        if num == 20 :
            hWords.append(word)
        elif num == -10 :
            sWords.append(word)
        elif num == 0 :
            nWords.append(word)

print('The positive keywords are', hWords)
print('The negative keywords are', sWords)
print('The neutral keywords are', nWords)
print('The sentiment of the tweet is', value)





