# import library
from flask import Flask

# Create a new flask app instance
app = Flask(__name__)


# Create flask routes
@app.route("/")
def hello():
    return "Hello, World!"


# create new route
@app.route("/about")
def about():
    name = "Duc"
    location = "Ha Noi"
    return f"My name is {name}, I live in {location}"


# Main function
if __name__ == "__main__":
    app.run(debug=True)
