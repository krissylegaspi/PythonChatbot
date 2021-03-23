weight = 25

# Ground Shipping
if weight <= 2:
    costGround = weight * 1.5 + 20
elif weight <= 6:
    costGround = weight * 3.00 + 20
elif weight <= 10:
    costGround = weight * 4.00 + 20
else:
    costGround = weight * 4.75 + 20
print("Ground Shipping $", costGround)

# Ground Shipping Premimum
costPremium = 125.00
print("Ground Shipping Premimium $", costPremium)

# Drone Shipping
if weight <= 2:
    costDrone = weight * 4.5
elif weight <= 6:
    costDrone = weight * 9.00
elif weight <= 10:
    costDrone = weight * 12.00
else:
    costDrone = weight * 14.25
print("Drone Shipping: $", costDrone)