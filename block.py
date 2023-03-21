import datetime as _dt
non=100000000
from hashlib import sha256
def hex(text):
    k=sha256(text.encode('ascii')).hexdigest()
    return k
def valid(name,lname):
    text=name+lname
    isvalid(text)
  


def isvalid(data):
    diff=1
    string ="0"*diff
    for nonce in range(non):
        text=data+str(nonce)
        m=hex(text)
        if(m.startswith(string)):
          print(m)
          
    

if __name__=="__main__":
   # print(hex("hello"))
    valid("rahul","kumar")