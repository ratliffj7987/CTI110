# A brief description of the project
# Date
# CTI-110 P5T2_FeetToInches 
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
