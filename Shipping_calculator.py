# Ground Shipping
# Weight of Package 	Price per Pound 	Flat Charge
# 2 lb or less 	$1.50 	$20.00
# Over 2 lb but less than or equal to 6 lb 	$3.00 	$20.00
# Over 6 lb but less than or equal to 10 lb 	$4.00 	$20.00
# Over 10 lb 	$4.75 	$20.00

weight = 8.4
cost_ground = None
cost_ground_preimum = 125.00 #Fixed Flat fee.

# Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4.00 + 20.00
else:
    cost_ground = weight * 4.75 + 20.00

print("The Total cost of your Shipping is: ", cost_ground)







# Ground Shipping Premium
#
# Flat charge: $125.00
#
# Drone Shipping
# Weight of Package 	Price per Pound 	Flat Charge
# 2 lb or less 	$4.50 	$0.00
# Over 2 lb but less than or equal to 6 lb 	$9.00 	$0.00
# Over 6 lb but less than or equal to 10 lb 	$12.00 	$0.00
# Over 10 lb
