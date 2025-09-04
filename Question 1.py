def encrypt_char(text, shift1, shift2):
    result = ''
    for char in text:
        if char.islower():  # a-z
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                base = ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:  # n-z
                shift = shift1 + shift2
                base = ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)  # <-- changed to + shift
        elif char.isupper():  # A-Z
            if char <= 'M':
                shift = shift1
                base = ord('A')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:  # N-Z
                shift = shift2 ** 2
                base = ord('A')
                result += chr((ord(char) - base + shift) % 26 + base)
        else:  # all other characters (numbers, symbols, spaces) remain unchanged
            result += char
    return result


def decrypt_char(text, shift1, shift2):
    result = ''
    for char in text:
        if char.islower():  # a-z
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                base = ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:  # n-z
                shift = shift1 + shift2
                base = ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)  # <-- changed to - shift
        elif char.isupper():  # A-Z
            if char <= 'M':
                shift = shift1
                base = ord('A')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:  # N-Z
                shift = shift2 ** 2
                base = ord('A')
                result += chr((ord(char) - base - shift) % 26 + base)
        else:  # all other characters remain unchanged
            result += char
    return result

def verify_decryption(original_text, decrypted_text):
    return original_text == decrypted_text

#User input 
if __name__ == "__main__":
    text = input("Enter filename to encrypt: ")
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

#Encryption process
    encrypted_text = encrypt_char(text, shift1, shift2)
    print("Encrypted text:")
    print(encrypted_text)
#Decryption process
    decrypted_text = decrypt_char(encrypted_text, shift1, shift2)
    print("Decrypted text:")
    print(decrypted_text)

#Verifing process
    if verify_decryption(text, decrypted_text):
        print("Decryption was successful, the original filename", text, "matches the encrypted filename.")
    else:
        print("Decryption failed. The texts do NOT match.")
