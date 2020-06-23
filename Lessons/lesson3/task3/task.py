# Add statements to complete the program.

from datetime import datetime
hour = datetime.now().hour

if hour > 12:
    print('Good Morning, World!')
    timeOfDay = 'morning'
elif 12>hour>6:
    print('Good Afternoon, World!')
    timeOfDay = 'afternoon'
else:
    print('Good Evening, World!')
    timeOfDay = 'evening'

# Place your code here

print("Good {}, world".format(timeOfDay))
