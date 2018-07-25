# CTI-110 
# P2HW2 - Area of Rectangles 
# Joseph Ratliff
# Date  6/23/2018


#the length and width of rectange 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

#the lengeth and width of rectange 2
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#areas of both recatngels
area1 = length1 * width1
area2 = length2 * width2

#Which is greater
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
