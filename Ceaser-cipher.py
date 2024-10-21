def encrypt(text: str, s: int) -> str:
    result = ""
    # Traverse text
    for char in text:
        if char.isupper():
            # Encrypt uppercase characters
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            # Encrypt lowercase characters
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text: str, s: int) -> str:
    result = ""
    # Traverse text
    for char in text:
        if char.isupper():
            # Decrypt uppercase characters
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            # Decrypt lowercase characters
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

# Check the functions
text = "ATTACKATONCE"
s = 3
print("Text : " + text)
print("Shift : " + str(s))
# Encrypt the text
CT = encrypt(text, s)
print("Cipher : " + CT)
# Decrypt the text
plain_text = decrypt(CT, s)
print("Plain text: " + plain_text)
