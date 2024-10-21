def rail_fence_encrypt(PT: str) -> str:
    ct1 = ''
    ct2 = ''
    # Traverse the plaintext and split it into two parts based on index
    for i in range(len(PT)):
        if i % 2 == 0:
            ct1 += PT[i]  # Even index characters
        else:
            ct2 += PT[i]  # Odd index characters
    # Concatenate the two parts to form the ciphertext
    CT = ct1 + ct2
    return CT

def rail_fence_decrypt(CT: str) -> str:
    half_len = (len(CT) + 1) // 2  # Adjusting to handle odd lengths
    ct1 = CT[:half_len]  # First half of the ciphertext
    ct2 = CT[half_len:]  # Second half of the ciphertext
    PT = ''
    # Reconstruct the plaintext by interleaving characters from both halves
    for i in range(half_len):
        PT += ct1[i]  # Add character from the first half
        if i < len(ct2):  # Check to avoid index out of range
            PT += ct2[i]  # Add character from the second half
    return PT

# Example usage
if __name__ == "__main__":
    PT = "Harry Potter"
    CT = rail_fence_encrypt(PT)
    print("Cipher Text:", CT)
    decrypted_PT = rail_fence_decrypt(CT)
    print("Decrypted Text:", decrypted_PT)
