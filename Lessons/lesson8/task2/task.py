# Replace the placeholders with code to handle the exception with the finnally clause and run the Python program

for i in range(10):
    try:
        print(7/i)
    except ZeroDivisionError:
        print('Divid by zero')
    finally :
        print(i)
