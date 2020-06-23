
#Elevator restrictions
floor = int(input("Floor: "))

if floor == 13 :
    print("Error: Please select a valid floor")
if floor <=0 or floor>20 :
    print("Error: Please select a valid floor")
else:
    actualFloor = floor
    if floor >13 :
        actualFloor = floor - 1
    print ("Floor", actualFloor)
