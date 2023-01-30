Lesson 3: Handling Forms with Flask

In this lesson, we will learn how to handle forms in a Flask web application. We will create a simple form that allows users to submit their name, and we will handle the form submission in our Flask application.

    First, we will create an HTML template for the form. In the templates directory, create a new file called form.html and add the following code:

html

<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form action="{{ url_for('form_submission') }}" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name">
        <input type="submit" value="Submit">
    </form>
</body>
</html>

This template creates a simple form with a single text input field for the user's name and a submit button. The form's action attribute is set to the URL of a route that we will create in our Flask application to handle the form submission. The method attribute is set to "post" to indicate that the form data should be sent as a POST request.

    Next, we will create a route in our Flask application to handle the form submission. In your app.py file, add the following code:

python

from flask import request

@app.route('/form', methods=['GET', 'POST'])
def form_submission():
    if request.method == 'POST':
        name = request.form['name']
        return 'Hello, ' + name
    return render_template('form.html')

This route handles both GET and POST requests. If the request is a GET request, the template for the form is rendered. If the request is a POST request, the name input from the form is extracted from the request object using the form attribute, and a greeting message is returned to the user.

    Finally, we need to add a link to the form in our main page template, so add this code in your index.html template file:

html

<a href="{{ url_for('form_submission') }}">Click here to submit your name</a>

    Now you can run the server by running the command flask run and test the application by visiting http://localhost:5000/ in your browser. You should see a link that says "Click here to submit your name". Clicking on that link should take you to the form where you can submit your name. After submitting the form, you should see a greeting message that includes your name.

You have now created a simple form and handled its submission in your Flask application. You can add more inputs fields, validation and also use post method to submit the form to the server and process it to store it in the database or do other operation on it.