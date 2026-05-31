def pin_extractor(poems):
    # List to store the final PIN codes for all poems
    secret_codes = []

    # Loop through each poem in the input list
    for poem in poems:
        secret_code = ''  # This will build the PIN for the current poem

        # Split the poem into individual lines
        lines = poem.split('\n')

        # Go through each line with its index
        for line_index, line in enumerate(lines):

            # Split the line into words
            words = line.split()

            # If the line has enough words for the current index
            # (i.e., we can safely access words[line_index])
            if len(words) > line_index:
                # Add the length of the selected word to the PIN
                secret_code += str(len(words[line_index]))
            else:
                # If not enough words exist, add '0' instead
                secret_code += '0'

        # Store the generated PIN for this poem
        secret_codes.append(secret_code)

    # Return all generated PIN codes
    return secret_codes


# -------------------- TEST DATA --------------------

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

poem3 = 'There\nonce\nwas\na\ndragon'

# Print PIN codes for all poems
print(pin_extractor([poem, poem2, poem3]))
