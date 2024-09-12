def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave non-alphabetical characters as is
        else:
            result += char

    return result


# Main program
if __name__ == "__main__":
    print("Caesar Cipher Encryption/Decryption Program")
    
    # User input
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    choice = input("Would you like to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    
    # Validate user choice and perform the operation
    if choice in ['encrypt', 'decrypt']:
        output = caesar_cipher(text, shift, mode=choice)
        print(f"The {choice}ed message is: {output}")
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
