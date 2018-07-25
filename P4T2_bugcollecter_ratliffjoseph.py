# made a program that adds the numbers the user inputs to calculate the total
# 7/12/2018
# CTI-110 P4T2 bug collector 
# JOSEPH RATLIFF


totalDays = 5
totalnumberofBugs = 0


for currentDay in range (1, totalDays + 1):
    bugscollected = int(input('How many bugs were collected on day' + \
                              str( currentDay ) + ':' ))
    totalnumberofBugs += bugscollected
    print()
    print('The total number of bug collected for all', totalDays, 'days is', \
          totalnumberofBugs )
