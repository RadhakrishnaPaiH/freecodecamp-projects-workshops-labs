def verify_card_number(card_number):
    # remove spaces and hyphens
    cleaned = ""
    for char in card_number:
        if char != " " and char != "-":
            cleaned += char

    # convert to list of integers
    digits = []
    for ch in cleaned:
        digits.append(int(ch))

    # apply Luhn algorithm from right to left
    total = 0
    length = len(digits)

    for i in range(length - 1, -1, -1):
        value = digits[i]

        # positions to double (every 2nd digit from right, excluding check digit)
        if (length - i) % 2 == 0:
            value = value * 2
            if value > 9:
                value = value - 9

        total += value

    # check validity
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
