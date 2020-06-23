
#All the same
def final(x):
    print(x)

def allTheSame():
    done = False
    a = input('Enter a value:')
    b = input('Enter a value:')
    c = input('Enter a value:')
    if a == b :
        if b == c :
            if a == c :
                done = True
            else:
                 done = False
        else:
            done = False
    else:
        done = False
    return done

final(allTheSame())




#counting vowels
def main(n):
    print(n)

def countVowels(str):
    vowels = 'aeiou'
    count = 0
    string = input('Please enter a string: ')
    string = string.lower()
    for i in string :
        if i in vowels:
            count = count + 1
    return count

main(countVowels(str))


