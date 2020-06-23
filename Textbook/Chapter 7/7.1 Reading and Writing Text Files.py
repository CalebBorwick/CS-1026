#Opening files - reading
infile = open('input.txt', "r")

#opening files - writing
outfile = open('input.txt', 'w')

#closing files
infile.close()
outfile.close()

#reading a file - readline method
line =infile.readline()
while line != '':
    #process the line
    line = infile.readline()

#converting file input
value = float(line)

#writing to a file
outfile.write('hello, world!/n')

#example
inputFileName = input('Enter file name: ')
outputFileName = input("Enter file name: ")
    #open the files
infile = open(inputFileName, "r")
outfile = open(outputFileName, "w")
    #read input and enter output
total = 0.0
count = 0

line = infile.readline()
while line != "":
    value = float(line)
    outfile.write("%15.2f/n" % value)
    total += value
    count += 1
    line = infile.readline()
#   Output the total and average
outfile.write("%15s /n" % '- - - - - - - - -')
outfile.write('Total: %8.2f/n' % total)
ave = total / count
outfile.write("Average: %6.2f/n" % ave)
     #close the file
infile.close()
outfile.close()
