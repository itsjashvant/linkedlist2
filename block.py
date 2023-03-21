from hashlib import sha256
from array import*
def hex(text):
    k=sha256(text.encode("ascii")).hexdigest()
    return k
class Block:
    def __init__(self,data,hash,prevhash):
        self.data=data
        self.hash=hash
        self.prevhash=prevhash

class Blockchain:
    def __init__(self):
        hash=hex("A")
        prevhash=hex("0")
        genesis=Block("first",hash,prevhash)
        self.chain=[genesis]
    def add(self,data):
        prevhash=self.chain[-1].hash
        text=prevhash+data
        hash=hex(text)
        block=Block(data,hash,prevhash)
        self.chain.append(block)

if __name__=="__main__":
    bc=Blockchain()
    bc.add("second")
    bc.add("third")
    bc.add("four")
    for block in bc.chain:
        print(block.__dict__)