from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.config['SECRET_KEY'] = "SECRET!"


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    username = db.Column(db.String(20),
                         nullable = False,)
    password = db.Column(db.String(30),
                         nullable = False)
    email = db.Column(db.String(50),
                         nullable = False)
    first_name = db.Column(db.String(50),
                         nullable = False)
    last_name = db.Column(db.String(50),
                         nullable = False)
