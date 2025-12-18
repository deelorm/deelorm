# Caesar Cipher program text

# Shows cipher run 
def caesar_run(text):  
    for _ in range(100 * len(text)):
        print('CIPHERING', end='')
        print('.'*10)
        print('')


# Encrpts or decrypts text with given mode and range
def caesar_cipher(text, mode=None, mode_range=None):
    print('....')
    # List of symbols 
    SYMBOL_TEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789.:;!,/\{}[]()?<>'\"|`@#$^&=+-*%"

    # Stores encrypted or decrypted text
    unplain_text = ''  
    
    # Console status message
    print('....')
    print('....')
    if mode.startswith('e'):
        print('Encrpting text..'.upper())
    elif mode.startswith('d'):
        print('Decrypting text..'.upper())

    # Converts text to number for encrytion or decryption
    for symbol in text:
        if symbol in SYMBOL_TEXT:
            symbol_num = SYMBOL_TEXT.find(symbol)

            if mode == "encrypt":
                symbol_num += int(mode_range)
            elif mode == "decrypt":
                symbol_num -= int(mode_range)
            
            if symbol_num < 0:  # Handles number underflow 
                symbol_num = symbol_num + len(SYMBOL_TEXT)
            elif symbol_num > 64:   # Handles number overflow
                symbol_num -= len(SYMBOL_TEXT)

            unplain_text += SYMBOL_TEXT[symbol_num]
        else:
            unplain_text += symbol

    # Console status message
    caesar_run(text)
    print('....')
    print('....')
    print('Rounding up....'.upper())
    if mode.startswith('e'):
        print('Encryption completed..'.upper())
    elif mode.startswith('d'):
        print('Decryption completed..'.upper())
    print('....')
    print('....')

    return unplain_text 


# Gets encrytion or decryption mode from user
def get_mode():
    print('....')
    print('Do you want to (e)ncrypt or (d)ecrypt?')     # Console message
    print('....')
    while True:
        user_mode = input('> ').lower()
        if user_mode.startswith('e'):
            user_mode = 'encrypt'
        elif user_mode.startswith('d'):
            user_mode = 'decrypt'
        else:
            print('Please enter either (e) or (d).')    # Console message
            continue
        print('....')
        print('Encryption/Decryption mode received.'.upper())   # Console status message

        return user_mode


# Gets range of decimal for encryption or decryption
def mode_range():
    # Console message
    print('....')
    print('Please enter range for text (e)ncrytion or (d)ecryption (0-64).')
    print('....')

    while True:
        user_range = input('> ').upper()
        if not user_range.isdecimal():
            print('Please enter decimal (0-64).')       # Console message
            continue

        # Console status message
        print('....')
        print('Range within bounds..'.upper())

        return user_range


# Gets text to be decrypted or encrypted
def symbol_text():
    # Console status message
    print('....')
    print('Please enter text to be (e)ncrypted or (d)ecrpted.')
    print('....')

    while True:
        text = input('> ').upper()
        if not text:
            print('Please enter text.')     # Console message
            continue

        # Console status message
        print('....')
        print('Text complete..'.upper())

        return text
     

# Prints program header text
def program_text():
    # Console status message
    print('*'*100)
    print('''
                    CAESAR STREAM CIPHER
    Casaer Cipher (stream cipher) encrytpion and decryption for text
    The program takes the following inputs:
    First Input: mode for (e)ncrytion or (d)ecryption 
    Second Input: decimal range for encrytion or decryption 
    Third Input: text to be encrypted or decrypted
    The program prints out the encrypted or decrypted text as output.
    ''')
    print('*'*100)


# Main program 
if __name__ == '__main__':
    # Function calls
    program_text()
    mode = get_mode()
    mode_range = mode_range()
    text = symbol_text()        
    caesar_text = caesar_cipher(text, mode, mode_range)     # Caesar cipher function call
    

    if mode.startswith('e'):
        print('')
        print('Encrypted text....'.upper())     # Console message
    elif mode.startswith('d'):
        print('Decrypted text....'.upper())     # Console message
    print('|'*len(text))

    print(caesar_text)      # Output text
    print('')