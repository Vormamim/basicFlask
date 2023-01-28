Lesson 1: Introduction to Flask

Objective:

    Understand what Flask is and its purpose
    Set up a basic Flask application
    Handle routes and render templates

Instructions:

    Install Flask by running the command pip install Flask in your command line.
    Create a new file called app.py and import Flask using the following code:

python

from flask import Flask

    Initialize a new Flask application by creating an instance of the Flask class. Give it a unique name, such as my_app.

python

app = Flask(__name__)

    Create a route that listens for incoming requests to the root URL. In this route, return a simple message, such as "Hello, World!".

python

@app.route('/')
def hello():
    return "Hello, World!"

    Add the following code to the bottom of your app.py file to run the development server:

python

if __name__ == '__main__':
    app.run()

    Run the application by running the command python app.py in your command line.
    Visit http://localhost:5000/ in your web browser to see the message "Hello, World!" displayed.

Explanation:

    Flask is a micro web framework for Python that allows developers to easily create web applications. It is lightweight, easy to learn, and easy to get started.
    The first step in creating a Flask application is to import the Flask class from the flask module.
    
    The Flask class is initialized by creating an instance of the Flask class and giving it a unique name. This is typically done using __name__ as an argument.
    In Flask, routes are used to handle incoming requests to different URLs. A route is created by using the @app.route decorator and specifying the URL it should listen for.
    In this example, the route is listening for requests to the root URL (/) and returns the message "Hello, World!" when a request is made to that URL.
    The development server is started by calling app.run() at the bottom of the file, after the routes have been defined.
    When you run the application with the command python app.py, it will start the development server and your application will be accessible on http://localhost:5000/.