# made a program that adds the numbers the user inputs to calculate the total
# 7/12/2018
# CTI-110 P4T2 bug collector 
# JOSEPH RATLIFF

total = 0 
usernumber = float(input('Enter the number? '))

while usernumber >-1:
    total = total + usernumber
    usernumber = float(input('Enter the next number'))

    print()
    print('the running total is:',total )
