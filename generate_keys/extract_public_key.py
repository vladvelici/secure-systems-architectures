from Crypto.PublicKey import RSA

# you need to run generate_keypair.py before running this, or you will get errors
# complaining about "FileNotFound private"

# read the file contents
with open("./my_private_key", "rb") as f:
    private_key_encoded = f.read()

# read the private_key (when we read the file, we get a list of bytes, we want
# to parse those bytes into a RSA key - this is what the next line does)
private_key = RSA.import_key(private_key_encoded)

# now the private_key variable is the private key

# extract the public key from the private key
public_key = private_key.publickey()

# now we just print the public key to the screen
print("This is the public key extracted from ./my_private_key private key file")
print()
print(public_key.export_key().decode())
