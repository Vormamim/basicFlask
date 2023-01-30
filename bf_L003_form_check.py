from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a route for the home page
@app.route('/') # route decorator for the index page   
def index():
    return render_template('indexB.html') # render a template

# Create a route for form submission
@app.route('/form_submission', methods=['POST'])
def form_submission():
    name = request.form.get('name')
    if name == "Jeff":
        return "Welcome Jeff!"
    else:
        return redirect(url_for('another_route'))

# Create a route for form submission
@app.route('/another_route')
def another_route():
    #return "This is another route"
    return render_template('another_route.html')    






if __name__ == '__main__':
    app.run()
