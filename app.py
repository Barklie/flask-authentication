from flask import Flask, request, render_template, redirect, jsonify
from models import db, connect_db, Cupcake
from sqlalchemy import text
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tweet_users_01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# debug = DebugToolbarExtension(app)


connect_db(app)

@app.route('/')
def redirect_to_register():
    return redirect('/register')

