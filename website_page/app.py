#import library
from flask import Flask

#Create a new flask app instance
app = Flask(__name__)

#Create flask routes
@app.route('/')
def hello():
    return 'Hello, World!'

#Main function
if __name__ == '__main__':
    app.run(debug=True)