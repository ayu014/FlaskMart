from market import app
from market.models import Item
from flask import render_template
from market.forms import RegisterForm, LoginForm




@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html",items = items)

@app.route("/register")
def register_page():
    form = RegisterForm()
    return render_template('register.html', form = form)

@app.route("/login")
def login_page():
    form = LoginForm()
    return render_template('login.html', form = form)
