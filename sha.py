from hashlib import sha256

def hex(text):
    k=sha256(text.encode('ascii')).hexdigest()
    return k
m=hex("hello")
print(m)