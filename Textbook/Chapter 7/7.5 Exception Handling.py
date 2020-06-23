try :
    filename = input("enter filename: ")
    infile = open(filename, 'r')
    line = infile.readline()
    for line in infile:
        value = int(line)
        print(value)
except IOError :
    print('Error: file not found')
except ValueError as exception :
    print('Error:', str(exception))

with open(filename, 'w') as outfile:
    #Write output to outfile

def readData(inFile) :
    line = inFile.readline()
    numberOfValues = int(line) # May raise a ValueError exception.
    data = []
    for i in range(numberOfValues) :
        line = inFile.readline()
        value = int(line) # May raise a ValueError exception.
        data.append(value)
# Make sure there are no more values in the file.
line = inFile.readline()
# Extra data in file
if line != "" :
    raise RuntimeError("End of file expected.")
return data
