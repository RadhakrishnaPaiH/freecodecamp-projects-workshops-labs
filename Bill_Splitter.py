# Running total starts at 0
running_total = 0

# Number of friends sharing the bill
num_of_friends = 4

# Cost of different food items
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Add all item costs to running total
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Calculate 25% tip based on total bill
tip = running_total * 0.25
print('Tip amount:', tip)

# Add tip to the running total
running_total += tip
print('Total with tip:', running_total)

# Split the final bill equally among friends
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)