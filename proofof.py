from hashlib import sha256
data="hello"
nonce=1
while(1):
    text=data+str(nonce)
    hash=sha256(text.encode('ascii')).hexdigest()
    if(hash[:2]=="".zfill(2)):
        print(hash)
        break
    nonce=nonce+1
