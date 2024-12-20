from market import app
from market.models import Item, User
from flask import render_template, redirect,url_for
from market.forms import RegisterForm, LoginForm
from market import db




@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html",items = items)

@app.route("/register", methods = ['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email = form.email.data,
                              password_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:                                   #If there are not any errors from the validations
        for error_msg in form.errors.values():
            print(f"There was an error with creating a user: {error_msg}")
    return render_template('register.html', form = form)

@app.route("/login")
def login_page():
    form = LoginForm()
    return render_template('login.html', form = form)
