def main():
    done = False
    list = []
    while not done :
        try :
            filename = input("Please enter the file name: ")
            data = open(filename,'r')
            total = 0
            for line in data:
                line = line.split(":")
                num = line[1]
                total = total + int(num)
                list.append(num)
            print(total)
            done = True
        except IOError :
         print("Error: file not found.")

        except ValueError :
         print("Error: file contents invalid.")

        except RuntimeError as error :
         print("Error:", str(error))

main()
