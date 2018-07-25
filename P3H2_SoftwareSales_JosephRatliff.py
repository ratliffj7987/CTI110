# CTI-110 
# P3HW2 - software sales 
# Joseph Ratliff
# Date  6/23/2018


#how many packages baouth
Salesnumber = int(input('Please enter the number of packages bought: '))
#price
PackagePrice = 99
if Salesnumber < 10:
    discount = 0;
elif Salesnumber < 20:
    discount = 0.10;
elif Salesnumber <50:
    discount = 0.20;
elif Salesnumber < 100:
    discount = 0.30;
else:
    discount = 0.40;

Subtotal = Salesnumber * PackagePrice

discountamount = discount * Subtotal
total = Subtotal - discountamount

print('Amont of discount: $' + format(discountamount, ',.2f') + \
      '\ntotal amount: $' + format(total, ',.2f'))
