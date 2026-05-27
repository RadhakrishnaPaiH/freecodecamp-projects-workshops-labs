# Caesar Cipher implementation for encryption and decryption

def caesar(text, shift, encrypt=True):
    # Validate shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Ensure shift is within valid range (1 to 25)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define lowercase alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse the shift direction
    if not encrypt:
        shift = -shift

    # Create shifted alphabet for substitution
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create translation table for both lowercase and uppercase letters
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Apply translation to text
    encrypted_text = text.translate(translation_table)

    return encrypted_text


# Wrapper function for encryption
def encrypt(text, shift):
    return caesar(text, shift)


# Wrapper function for decryption
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# Encrypted message (Caesar cipher with shift 13)
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

# Decrypt the message
decrypted_text = decrypt(encrypted_text, 13)

# Print result
print(decrypted_text)