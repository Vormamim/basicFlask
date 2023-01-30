Lesson 2: Flask Templates

Objective:

    Understand Jinja2, Flask's built-in templating engine
    Create templates and pass data to templates

    Jinja2 is a templating engine that is built into Flask and is used to create dynamic templates for your web applications.

    Templates are HTML files that include special syntax that allows you to insert data from your application into the HTML.

    In Jinja2, templates can be extended using the {% extends %} template tag. In this example, index.html extends base.html.

    Blocks are used to define areas in the base template that child templates can override. In this example, base.html has two blocks: title and content. These blocks are overridden in index.html.
    The render_template function is used to render a template and return the rendered HTML to the client. In this example, the index.html template is rendered and returned when a request is made to the root route.
    When you run the application with the command python app.py, it will start the development server and your application will be accessible on http://localhost:5000/.

Instructions:

    Create a new folder called **templates** in your Flask project's root directory.
    In this folder, create a new file called base.html which will serve as the base template for your other templates.
    
    In base.html, include the following code to create a basic structure for your templates:

html

<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}Default Title{% endblock %}</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>

    Create a new template file called index.html and include the following code:

html

{% extends 'base.html' %}
{% block title %}Home{% endblock %}
{% block content %}
  <h1>Welcome to our website</h1>
{% endblock %}

    In your app.py file, import the render_template function from Flask and use it to render the index.html template in the root route:

python

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

    Run the application by running the command python app.py in your command line.
    Visit http://localhost:5000/ in your web browser to see the message "Welcome to our website" with a title of "Home" displayed.

more:
[title]https://www.youtube.com/watch?v=4L_xAWDRs7w&list=PLZoTAELRMXVPBaLN3e-uoVRR9hlRFRfUc
    