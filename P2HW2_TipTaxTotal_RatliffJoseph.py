
# CTI-110 
# P2HW2 - Tip Tax Total 
# Joseph Ratliff
# Date  6/17/2018
#


# Charge of the food
FoodCharge = float(input("Charge"))

# Calcualte Tip
Tip = FoodCharge * .18

#salse tax
SalesTax = FoodCharge * .18
                

#total
Total = FoodCharge + Tip + SalesTax
print('Food Charge; $'+ format( FoodCharge, ',.2f'), 'Tip: $' + \
      format(Tip, ',.2f'), "SalesTax: $" + format( SalesTax, " ,.2f"), \
'Total: $' + format( Total, ',.2f'), sep = "\n" )



