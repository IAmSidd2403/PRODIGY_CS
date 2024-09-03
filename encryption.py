

def caesar_cipher(text, shift, direction):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if direction == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += shifted_char
        else:
            result += char
    
    return result

text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
direction = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

output = caesar_cipher(text, shift, direction)

print(f"Result: {output}")
