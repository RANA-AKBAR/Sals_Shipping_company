
weight = 1.5
cost_ground = None
cost_ground_premium = 125.00 
cost_drone = None




# Ground Shipping
# Weight of Package     Price per Pound     Flat Charge
# 2 lb or less  $1.50   $20.00
# Over 2 lb but less than or equal to 6 lb  $3.00   $20.00
# Over 6 lb but less than or equal to 10 lb     $4.00   $20.00
# Over 10 lb    $4.75   $20.00

# Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4.00 + 20.00
else:
    cost_ground = weight * 4.75 + 20.00

print("The Total cost of your Standard Ground Shipping is: ", cost_ground)




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

#Fixed Flat fee.

print("The Total cost of your Premium Ground Shipping is: ", cost_ground_premium)


# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
# Drone Shipping
# Weight of Package   Price per Pound     Flat Charge
# 2 lb or less    $4.50   $0.00
# Over 2 lb but less than or equal to 6 lb    $9.00   $0.00
# Over 6 lb but less than or equal to 10 lb   $12.00  $0.00
# Over 10 lb  $14.25  $0.00


if weight <= 2: 
    cost_drone = weight * 4.50
elif weight >2 and weight <= 6:
    cost_drone = weight * 9.00
elif weight >6 and weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25


print("The Total cost of your Drone Shipping is: ", cost_drone)
