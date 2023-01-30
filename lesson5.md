Lesson 5: Retrieving Data from a Database

In this lesson, we will learn how to retrieve data from a database in our Flask application.

Databases are by far the most common and most efficient way of handing data.
This lesson helps you get started with SQL (structured query language)

SQL, or Structured Query Language, is a programming language used for managing and manipulating relational databases. It is used to insert, update, retrieve, and delete data stored in a database. SQL statements are used to create and modify database structures, such as tables and indexes, as well as to manipulate data within those structures. Some common SQL commands include SELECT, INSERT, UPDATE, DELETE, and CREATE. SQL is widely used in many different types of software and applications, including web-based systems, data analysis tools, and business intelligence software.


To run SCSS in Visual Studio Code, you will need to install an extension for it. One popular extension is "Live Sass Compiler". Once the extension is installed, you can configure it by going to the settings (File > Preferences > Settings) and searching for "Live Sass Compiler" to access the options. In the settings, you can specify the location of your SCSS and CSS files, and set the compiler options. Once you have set it up, you can use the "Watch Sass" command to start the compilation process. The compiled CSS will then be saved to the specified location.




Install the required packages:


pip install flask-sqlalchemy

or 

py -m pip install flask-sqlalchemy

    
Import the necessary modules at the beginning of your python file:


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

    Create an instance of the SQLAlchemy class, and set the database URI in the application's config:

python

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

    Create a model for the users table:

python

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    Create a route to retrieve data from the users table:

python ----

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

    Create a template to display the retrieved data. In this example, the template is called users.html and is located in the templates folder:

html ----

<table>
  <tr>
    <th>Name</th>
    <th>Email</th>
  </tr>
  {% for user in users %}
  <tr>
    <td>{{ user.name }}</td>
    <td>{{ user.email }}</td>
  </tr>
  {% endfor %}
</table>

    Finally, create the database by running the following command:

python ---

db.create_all()

    Now you can run your application and visit the /users route to see the data retrieved from the database.