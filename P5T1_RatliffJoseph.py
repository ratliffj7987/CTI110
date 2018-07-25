# CTI-110 
# P5T1 - Kilometer Converter
# Joseph Ratliff
# Date  7/8/2018
#

#user input
def askuserforKilometers():
    userKilometers = float(input('Please enter the distance i kilometers: '))

    return userKilometers

def convertToMiles(userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askuserforKilometers()
    milesConverted = convertToMiles( userKilometersTyped )

    print( userKilometersTyped, 'kilometers converted to miles', \
           milesConverted, 'miles')

main()
