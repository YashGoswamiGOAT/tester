from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def ind():
    open("yash.txt","w").write("YASH ROCKS")
    return "Hello"

@app.route("/yash")
def red():
    return str(requests.get("https://yashgoswamigoat.pythonanywhere.com/webservice/notifications").text)+str(open("yash.txt","r").read())

if __name__=="__main__":
    app.run()
