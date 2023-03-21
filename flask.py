from hashlib import sha256


def mine(self,text):
    nonce=4
    index=1
    string="0"*nonce
    while(True):
        text1=str(index)+text
        p=hex(text1)
        if p.startswith(string):
            return p
        else :
            index=index+1
        

        


def hex(text):
    k=sha256(text.encode('ascii')).hexdigest()
    return k



# this is the output block for the trasport that want to see

def output(cha):
    for chai in cha:
        print(chai.__dict__)
        


#this is the checker block to show is the block  is valid or not  for the transport

def checker(selfchains,newactive,trans):
    
        if((selfchains!=trans)&(selfchains.active1st==False)):
            if(newactive==True):
             return True
        else:
            return False



#this is the block to check is the request full by the user or not

def checker1(selfchain1,newcative,trans1):
    if((selfchain1!=trans1)&selfchain1.active2nd==False):
        return True
    else:
        return False




#this is the output for the second 

def out(self,tr):
    for a in tr:
        print(a.__dict__)



class Block:
    def __init__(self,name,amount,location,type,active1st,active2nd,hash,prevhash):
        self.name=name
        self.amount=amount
        self.location=location
        self.type=type
        self.active1st=active1st
        self.active2nd=active2nd
        self.hash=hash
        self.prevhash=prevhash



class Blockchain:
        def __init__(self):
          prevhash=hex('0')
          hash=hex("first")
          genesis=Block("genesis",0,"none","none",True,True,hash,prevhash)
          self.tempchain=[genesis]
          self.trans=[genesis]
          self.user=[genesis]
       
       
       
       
       
       
        def request(self,name,amount,place,type,active1st,active2nd):
           prevhash=self.tempchain[-1].hash
           text=name+str(amount)+place+type+str(active1st)+str(active2nd)
           hash1=hex(text)
           hash=mine(self,hash1)
           block=Block(name,amount,place,type,active1st,active2nd,hash,prevhash)
           self.tempchain.append(block)
           output(self.tempchain)
        
        
        
        
        def Transport(self,newactive):
          
           
            for b in self.tempchain:
                for c in self.trans:
                      k= checker(b,newactive,c)
                      if(k==True):
                        self.trans.append(b)
                        print(b.__dict__)

            #output(self.trans)
            
                    
               
        #this is block to check the order by the seller or buyer
        
        def getrequest(self,newcative4):
              for b in self.tempchain:
                for c in self.user:
                    k=checker1(b,newcative4,c)
                    if k==True:
                        self.user.append(b)
                        print(b.__dict__)
                        break
            
             

            # this is the bolck to check the ans
        #def ans(self):
          #  for a in self.tempchain:
               # print(a.__dict__)
        

if __name__=="__main__":
    bc=Blockchain()
    bc.request("rahul",2500,"india","buyer",True,True)
    bc.request("mohan",200,"india","buyer",True,False)
    bc.request("sohan",2100,"india","buyer",True,True)
    bc.request("gita",2300,"india","seller",False,True)
    #for b in bc.tempchain:
       # print(b.__dict__)

    a=input("input the number")
    #bc.ans();
    bc.Transport(a)
    #bc.getrequest(a)
    #bc.getrequest()
  
        


         


