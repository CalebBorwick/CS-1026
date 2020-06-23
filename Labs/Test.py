def main():
    done = False
    while not done :
        try :
            filename = input("Please enter the file name: ")
            data = readFile(filename)
            total = 0
            for line in data:
                line = line.split(":")
                num = line[1]
                total = total + int(num)
            print(total)
            done = True

        except IOError :
            print("Error: file not found.")

        except ValueError :
            print("Error: file contents invalid.")

        except RuntimeError as error :
            print("Error:", str(error))

def readFile(filename):
    inFile = open(filename, 'r')
    try :
        return inFile
    finally :
        inFile.close()

main()
