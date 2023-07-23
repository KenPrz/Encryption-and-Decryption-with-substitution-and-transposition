def substitution_encrypt(userMessage, key):
    encrypted_message = ""
    for char in userMessage:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message

def substitution_decrypt(encryptedMessage, key):
    decrypted_message = ""
    for char in encryptedMessage:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

def transposition_encrypt(userMessage, key):
    encrypted_message = ""
    for col in range(key):
        pointer = col
        while pointer < len(userMessage):
            encrypted_message += userMessage[pointer]
            pointer += key
    return encrypted_message

def transposition_decrypt(encryptedMessage, key):
    decrypted_message = [''] * len(encryptedMessage)
    col = 0
    for pointer in range(len(encryptedMessage)):
        decrypted_message[pointer] = encryptedMessage[col]
        col += key
        if col >= len(encryptedMessage):
            col = pointer + 1
    return ''.join(decrypted_message)


userMethod = int(input('what would you like to do? \n1. Encrypt\n2. Decrypt\nChoice: '))
if userMethod == 1:
    userMessage = str(input("enter your message: "))
    encryptionMethod = int(input('how would you like your message to be encrypted?\n1. Substitution \n2. Transposition\nChoice: '))
    if encryptionMethod == 1:
        key = int(input("Enter the substitution key (an integer): "))
        print('encrypted message:', substitution_encrypt(userMessage, key))
    elif encryptionMethod == 2:
        key = int(input("Enter the transposition key (an integer): "))
        print('encrypted message:', transposition_encrypt(userMessage, key))
elif userMethod == 2:
    userMessage = str(input("enter the message you want to decrypt: "))
    encryptionMethod = int(input('how would you like your message to be decrypted?\n1. Substitution \n2. Transposition\nChoice: '))
    if encryptionMethod == 1:
        key = int(input("Enter the substitution key (an integer): "))
        print('decrypted message:', substitution_decrypt(userMessage, key))
    elif encryptionMethod == 2:
        key = int(input("Enter the transposition key (an integer): "))
        print('decrypted message:', transposition_decrypt(userMessage, key))

#written 05-23-23