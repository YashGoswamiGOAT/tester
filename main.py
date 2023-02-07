from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def ind():
    return "Hello"

@app.route("/yash")
def red():
    return str(requests.get("https://yashgoswamigoat.pythonanywhere.com/webservice/notifications").text)

if __name__=="__main__":
    app.run()