from hashlib import sha256
nonce=1000000000000
def hex(text):
    k=sha256(text.encode('ascii')).hexdigest()
    return k
def mine(blockno,hash,prehash,diffi):
    deff_no="0"*diffi
    for non in range(nonce):
        text=str(blockno)+hash+prehash+str(non)
        p=hex(text)
        if p.startswith(deff_no):
            print("yahh i have mine the block")
            return p
if __name__=="__main__":
    l=mine(4,"drbdbfdnvk","008ea061e26c48b23d20868938ad6c9f37c8bc3e9cc9548738197e6f0ee62bf1",4)
    print(l)