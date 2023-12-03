# import library
from flask import Flask, render_template

# Create a new flask app instance
app = Flask(__name__)


# Create flask routes
@app.route('/')
def hello():
    return render_template('index.html')  # Utilizes the file base.html


# create new route
@app.route('/about')
def about():
    name = 'Duc'
    location = 'Ha Noi'
    return render_template('about.html', name=name, location=location)


# Main function
if __name__ == '__main__':
    app.run(debug=True)
