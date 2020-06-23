#Ian Borwick Assignment 2
#Volume Calculator for cube, pyrimid and ellipsoid

#import modules
import math

#determining shape
done = False
properShape = ['cube', 'pyrimid', 'ellipsoid', 'quit']

#lists
cubeList = []
pyrimidList = []
ellipsoidList = []

#shape loop
while not done :
    shape = input('Please choice a shape: A cube or a pyrimid or an ellipsoid or enter quit to leave:')
    if shape.lower() == 'quit' :
        done = True
    if shape.lower() not in properShape :
        print('Please enter a valid input')
#Cube
     #if statement to initialize into cube
    if shape.lower() == 'cube' :
        # Cube input function
        def cube() :
            sideLength = int(input('Please enter the side legnth of the cube:'))
            resultC = cubeVolume(sideLength)
            print('A cube with side length of', sideLength, 'has volume', round(resultC,1))
            cubeList.append(round(resultC,1))
        #Calaculation for cube volume function
        def cubeVolume(sideLength) :
            volume = (sideLength*sideLength*sideLength)
            return volume
        #Cube call
        cube()

#Pyrimid
    #if statement to initialize into pyrimid
    if shape.lower() == 'pyrimid' :
        #Pyrimid input function
        def pyrimid() :
            base = (int(input('Please enter the length of the base: ')))
            height = (int(input('Please enter the height if the pyrimid: ')))
            resultP = pyrimidVolume(base,height)
            print('The pyrimid has a volume of',round(resultP, 1), 'with a base of', base, 'and a height of', height)
            pyrimidList.append(round(resultP,1))
        #Calculation for pyrimid volume function
        def pyrimidVolume(base,height):
            volume = ((1/3) * (base * base) * (height))
            return volume
        #Pyrimid Call
        pyrimid()

#Ellipsoid
    #if statement to initailze into ellipsoid
    if shape.lower() == 'ellipsoid' :
        #Ellipsoid input function
        def ellipsoid() :
            radius1 = int(input('Please enter radius 1: '))
            radius2 = int(input('Please enter radius 2: '))
            radius3 = int(input('Please enter radius 3: '))
            resultE = ellipsoidVolume(radius1,radius2,radius3)
            print('The volume of the ellipsoid is', round(resultE, 1), 'with radius of', radius1,',', radius2, ' and', radius3 )
            ellipsoidList.append(round(resultE,1))
        #Calculation for ellipsoid volume function
        def ellipsoidVolume(radius1,radius2,radius3) :
            volume = (4/3)*(math.pi)* radius1 * radius2 * radius3
            return volume
        #Ellipsoid call
        ellipsoid()

#Final output
    elif shape.lower() == 'quit' :
        if cubeList != [] or pyrimidList != [] or ellipsoidList != []:
            #Output statements
            print('You have come to the end of the session')
            print('The volumes calculated for each shape are shown below')
            #Cube output
            if cubeList != [] :
                cubeList = sorted(cubeList)
                print('Cube:', end=" ")
                for i in range (len(cubeList)) :
                    if i == len(cubeList)-1 :
                        print(cubeList[i])
                    else:
                        print(cubeList[i], end=", ")
            else :
                print('Cube: No computations for this shape')
            #Pyrimid output
            if pyrimidList != [] :
                pyrimidList = sorted(pyrimidList)
                print('Pyrimid:', end=" ")
                for i in range (len(pyrimidList)) :
                    if i == len(pyrimidList)-1 :
                        print(pyrimidList[i])
                    else:
                        print(pyrimidList[i], end=", ")
            else :
                print('Pyrimid: No computations for this shape')
            #Ellipsoid output
            if ellipsoidList != []:
                ellipsoidList = sorted(ellipsoidList)
                print('Ellipsoid:', end=" ")
                for i in range (len(ellipsoidList)) :
                    if i == len(ellipsoidList)-1 :
                        print(ellipsoidList[i])
                    else:
                        print(ellipsoidList[i], end=", ")
            else :
                print('Ellipsoid: No computations for this shape')
#Extra condition
        if cubeList == [] and pyrimidList == [] and ellipsoidList == [] :
            print('You have come to the end of the session')
            print(('You did not perform any volume calculations'))


