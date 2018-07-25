# A brief description of the project
# Date
# CTI-110 P5T2_FeetToInches 
# JOSEPH RATLIFF



def feetToinches( userFeet ):
    inches = ( userFeet / 1 ) * 12
    return inches

def main():
    userFeet = float(input('Please ent the number of feet: '))
    print()
    inches = feetToinches( userFeet )
    print( userFeet, 'Feet converted to inches is', format( inches, '.2f' ), 'inches')

main()
