# 7/12/2018
# CTI-110 P4HW3 Factorial 
# JOSEPH RATLIFF

userinteger = int(input('Please enter a number'))

while userinteger < 1:
    userinteger = int(input('Please enter a positive number: '))

factorial = 1

for currentnumber in range( 1, userinteger + 1):
    factorial = factorial * currentnumber

print()
print('The factorial of', userinteger, 'is', factorial )
