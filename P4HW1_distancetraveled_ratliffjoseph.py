# made a program that uses a for loop to break down the distance traveled every hour
# 7/12/2018
# CTI-110 P4T2 bug collector 
# JOSEPH RATLIFF

vehiclespeed = float(input('What is the speed'))
timetraveled = int(input('how many hours taveled?: '))

print()

print('Hour', '\tDistance Traveled')
for currenthour in range(1, timetraveled + 1):
      distancetraveled = vehiclespeed * currenthour
      print( currenthour, '\t',distancetraveled )
