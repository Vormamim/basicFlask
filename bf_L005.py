from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    with app.app_context():
        db.create_all()
        user1 = User(name='John', email='john@example.com')
        user2 = User(name='Jane', email='jane@example.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        users = User.query.all()
        return render_template('bootstrapUsers.html', users=users)

@app.route('/clear-database', methods=['POST'])
def clear_database():
    User.query.delete()
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()
