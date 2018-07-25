# CTI-110 
# P3HW1 - Age Classifier 
# Joseph Ratliff
# Date  6/23/2018

# user age
userAge = int(input('Please enter your age: '))
# if you are an ifant 
if userAge <= 1:
    print('\nYou are an infant')
#if you are a child
elif userAge < 13:
    print('\nYou are an child')
#if you are a teenager
elif userAge < 20:
    print('\nYou are an teenager')
#the final elif statement you must be and adult
elif userAge >= 20:
          print('\nYou are an Adult')
