# Import libraries
import hashlib
import hmac

# Data
update_bytes = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Suspendisse tristique condimentum viverra. Nulla accumsan orci risus, non congue lacus \
feugiat id.'

# Secret key
password = b'402xy5#'

# Generate cryptographic hash using md5
my_hmac = hmac.new(update_bytes, password, hashlib.md5)

print("The first digest: " + str(my_hmac.digest()))
print("The Canonical Name: " + my_hmac.name)
print("Block size: " + str(my_hmac.block_size) + " bytes")
print("Digest size: " + str(my_hmac.digest_size) + " bytes")

# Create a copy of the hmac object
my_hmac_cpy = my_hmac.copy()
print("The Copied digest: " + str(my_hmac_cpy.digest()))
