# Description: Hello World
from flask import Flask # import Flask class
app = Flask(__name__) # 
@app.route('/') # route decorator
# define a function to handle the route
def hello_world(): 
    return 'Hello, World!' # return a string
# run the application
if __name__ == '__main__':
    app.run()