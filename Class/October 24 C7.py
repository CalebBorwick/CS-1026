#read
infile = open("input.txt", "r")
#write
outfile = open('input.txt','w')
#close file
infile.close()
outfile.close()

#reading a file
line= infile.readline()

#read all lines
line = infile.readline()
while line!= "" :
    line= infile.readline()
#writing to a file
outfile.write()('hello,world!/n')


#Complete example
inputFile = open("lyric.txt", "r")
for line in inputFile :
    line = line.rstrip()
    wordList = line.split()
    for word in wordList :
        word = word.rstrip(".,?!")
        print(word)
inputFile.close()
