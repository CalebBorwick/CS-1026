#pulse check

def multiplesSet(maxValue, num1, num2):
    list = set()
    for i in range(maxValue+1):
        if i % num1 == 0 :
            list.add(i)
        if i % num2 == 0:
            list.add(i)
    print(list)

multiplesSet(8,2,3)

