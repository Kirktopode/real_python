# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url

@app.route("/")
@app.route("/hello")


# define the view using a function, which returns a string
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/test/<sq>")
def search(sq):
    return "OH NO, THE " + sq.upper()

@app.route("/integer/<int:val>")
def int_type(val):
    print (val - 3)
    return "hyep"

@app.route("/float/<float:val>")
def float_type(val):
    print (val + 9.9)
    return "hyep"

@app.route("/path/<path:val>")
def path_type(val):
    print (val)
    return "hyep"

# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "sweety_beety" :
        return "Hello, {}".format(name), 200
    else :
        return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
