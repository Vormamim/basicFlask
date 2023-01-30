Lesson 4: Working with Forms

In this lesson, you will learn how to work with forms in Flask. Specifically, you will learn how to:

    Create a form in HTML
    Retrieve form data in Flask
    Validate form data
    Display error messages

Forms are the most common inputs from users. Users tend to make mistakes.
We want to not let the user 'see' the form, so we generate it dynamically.

Here is an example of how you can create a simple form in HTML:

<form action="{{ url_for('form_submission') }}" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <br>
    <input type="submit" value="Submit">
</form>

In this example, we have created a form with two fields: "Name" and "Email". The form's action is set to the route form_submission, and the method is set to POST.

To retrieve the form data in Flask, you can use the request.form object, like this:

name = request.form.get('name')
email = request.form.get('email')

To validate the form data, you can use a combination of built-in functions such as len(), str.isalpha(), and str.isalnum() to check the length and type of the data entered.

About RE (regular expression)
This is built into python, so you don't need to pip install or add the extension.

The re module includes several functions and methods for working with regular expressions. Some of the most commonly used functions include search, findall, sub, split, and compile. The compile function is used to create a regular expression pattern object, which can be used to match and search for patterns in strings.

In the code, I am using the re.compile() function to create a regular expression pattern object, with the pattern ^(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$. Then, I am using the match() method on the pattern object to check if the name field matches the pattern. If it matches, the form_submission function will return "password valid". If it doesn't, it will return "password not valid".

You can also use other functions like finditer, fullmatch, subn and many more that are provided by the re module.

You do not need to pip install re, as it is a built-in module in Python, so you can use it out of the box. The re module is part of the Python standard library, which means that it is included with the installation of Python, and is available for you to use without needing to install it separately..

This is a handy program you can use to validate user-log ins.
