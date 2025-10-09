from flask import Flask, render_template

app = Flask(__name__)

# A route to the home page of line the app 
@app.route('/')
def index():
    return " Welcome to My FLask App Home Page! "

# A new route to the 'greet' page of the app
@app.route("/greet/<name>")
def GreetPage(name):
    return render_template("index.html", name  = name)


if __name__ =='__main__':
    app.run(debug = True)