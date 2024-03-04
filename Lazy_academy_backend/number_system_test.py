from flask import Flask,render_template
from random import randrange

app=Flask(__name__)

@app.route("/")
def home():
    a=randrange(1,1000)
    b=bin(a)[2:]
    c=randrange(1,1000)
    d=bin(a)[2:]
    print(type(b))
    print(f"{b}+{d}={bin(a+c)[2:]}")
    text="Congratulations !!!!"
    return render_template("index.html",context={"text":text})

if __name__=="__main__":
    app.run(debug=True)
