from Crypto.PublicKey import RSA

# generate a new private key:
private_key = RSA.generate(2048)

# extract public key from the private key:
public_key = private_key.publickey()


# encode public key in a format that can be saved to a file
public_key_encoded = public_key.export_key()

# save the public key to a file:
with open("./my_public_key", "wb") as f:
    f.write(public_key_encoded)
    f.write(b"\n") # this write just adds a newline at the end of the file

# encode and save private key
private_key_encoded = private_key.export_key()

# save the public key to a file:
with open("./my_private_key", "wb") as f:
    f.write(private_key_encoded)
    f.write(b"\n") # this write just adds a newline at the end of the file
