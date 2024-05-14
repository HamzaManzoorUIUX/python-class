from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/login")
def login():
    return "<p>Hello, World! you are logeddin into system</p>"
@app.route("/login2")
def login2():
    return render_template("login.html",userName="Hamza Manzoor",password="123456")
app.run(debug=True)