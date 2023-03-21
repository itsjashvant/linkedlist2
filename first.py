from flask import Flask
from hashlib import sha256

k=sha256("hello".encode('ascii')).hexdigest()
print(k)










app=Flask(__name__)
@app.route("/")
def hello():
    return "hello"
@app.route('/home')
def home():
    return "home"
@app.route('/aboutus')
def about():
    return "i am jashvant"
if __name__=="__main__":
    app.run()