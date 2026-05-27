# Base ticket price
base_price = 15

# User details
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# Check basic eligibility
if age > 17:
    print('User is eligible to book a ticket')

# Check eligibility for evening shows based on age
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Membership and weekend status
is_member = False
is_weekend = False

# Calculate discount
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print('Discount:', discount)

# Extra charges based on weekend or show time
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)

# Final booking condition check
if age >= 21 or (age >= 18 and (show_time != 'Evening' or is_member)):
    print('Ticket booking condition satisfied')

    # Service charge based on seat type
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    print('Service charges:', service_charges)

    # Final ticket price calculation
    final_price = base_price - discount + extra_charges + service_charges
    print("Final price of ticket:", final_price)

else:
    print('Ticket booking failed due to restrictions')