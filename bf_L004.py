
from flask import Flask, request, render_template
import re


app = Flask(__name__)

# Create a route for the home page
@app.route('/') # route decorator for the index page   
def index():
    return render_template('indexC.html') # render a template

# Create a route for form submission
@app.route('/form_submission', methods=['POST'])

def form_submission():
    name = request.form.get('name')
    email = request.form.get('email')

    pattern = re.compile("^(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$")
    if pattern.match(name):
        return "password valid"
    else:
        return "password not valid"
    # Do something with the name and email




if __name__ == '__main__':
    app.run()