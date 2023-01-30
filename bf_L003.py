from flask import Flask, render_template, request

app = Flask(__name__)

# Create a route for the home page
@app.route('/') # route decorator for the index page   
def index():
    return render_template('indexB.html') # render a template

# Create a route for form submission
@app.route('/form_submission', methods=['POST'])
def form_submission():
    # Get the value of the 'name' field from the form
    name = request.form['name']
    # Return a greeting message with the passed name
    return f"Hello {name}, Form Submitted Successfully!"

if __name__ == '__main__':
    app.run()
