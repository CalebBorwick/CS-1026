import math
print(math.pi)
def main() :
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)
    print('A cube with side length 2 has volume', result1)
    print('A cube with side length 10 has volume',result2)

def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume
main()



