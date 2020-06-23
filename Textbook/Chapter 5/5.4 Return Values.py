

def numberProblem() :
    digit = int(input('Enter a value between 1 and 9: '))
    if digit == 1 : return 'one'
    if digit == 2 : return 'two'
    if digit == 3 : return 'three'
    if digit == 4 : return 'four'
    if digit == 5 : return 'five'
    if digit == 6 : return 'six'
    if digit == 7 : return 'seven'
    if digit == 8 : return 'eight'
    if digit == 9 : return 'nine'
print(numberProblem())

def main() :
    print('Volume', pVolume(9,10))
    print('Expected: 300')
    print('Volume', pVolume(1,10))
    print('Expected: 0')
def pVolume (base,height) :
    baseArea = base * base
    return height * baseArea / 3
main()
