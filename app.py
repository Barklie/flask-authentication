from flask import Flask, request, render_template, redirect, session, flash
from models import db, connect_db, User, Feedback
from forms import addUserForm, loginUserForm, userFeedbackForm
from sqlalchemy import text
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://barkliegriggs:12am@localhost:5432/tweet_users_01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

bcrypt = Bcrypt()


@app.route('/')
def redirect_to_register():
    """Redirect to register page."""
    return redirect('/register')


@app.route('/register', methods=["GET", "POST"])
def register():
    """Rregister a new user"""
    form = addUserForm()
    if request.method == 'GET':

        return render_template('register.html', form=form)

    else:
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.last_name.data

            new_user = User.register(
                username, password, email, first_name, last_name)

            db.session.add(new_user)
            try:
                db.session.commit()
            except IntegrityError:
                form.username.errors.append(
                    'Username taken.  Please pick another')

            session['user_id'] = new_user.id
            flash('Welcome! Successfully Created Your Account!', "success")

        return redirect('/secret')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = loginUserForm()
    print("post form***********")
    if "user_id" not in session:
        if request.method == 'GET':

            return render_template('login.html', form=form)
        else:
            print("else")
            if form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                user = User.authenticate(username, password)
                if user:
                    flash(f"Welcome Back, {user.username}!", "primary")
                    session['user_id'] = user.id
                    session['username_auth'] = user.username
                    return redirect(f"/user/{username}")
                else:
                    form.username.errors = ['Invalid username/password.']
                    return render_template('login.html', form=form)
    else:
        session.pop("user_id")
        return render_template('login.html', form=form)


@app.route("/user/<username>")
def user(username):
    """shows feedback created by user"""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("secret.html")


@app.route("/logout")
def logout():
    """ Logs user out and redirects to homepage. """

    session.pop("user_id")

    return redirect("/")


@app.route("/user/<username>/feedback/add", methods=["GET", "POST"])
def user_feedback(username):
    form = userFeedbackForm()
    if request.method == 'GET':

        if "user_id" not in session:
            flash("You must be logged in to view!")
            return redirect("/")

        else:
            return render_template("feedback.html", form=form)
    else:
        if "user_id" not in session:
            flash("You must be logged in to view!")
            return redirect("/")

        else:
            if form.validate_on_submit():
                title = form.title.data
                content = form.content.data

                new_feedback = Feedback(
                    title=title, content=content)

                db.session.add(new_feedback)
                try:
                    db.session.commit()
                except IntegrityError:
                    form.feedback.errors.append(
                        'Fill out both boxes. Please try again')

        return redirect('/user/<username>/feedback')
