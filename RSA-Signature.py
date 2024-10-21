from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Simulated document content
original_document = b"This is the original document content."
modified_document = b"This is the modified document content."

# Hash the document content
original_hash = SHA256.new(original_document)
modified_hash = SHA256.new(modified_document)

# Create a signature using the private key
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(original_hash)

# Verify the signature using the public key with the modified content
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(original_hash, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature is invalid.")
