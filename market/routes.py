from logging import info
from os import name
from market import app
from market.models import Item, User
from flask import request, render_template, redirect,url_for, flash,get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from market.forms import RegisterForm, LoginForm, SellItemForm, BuyItemForm
from market import db




@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/market", methods=['GET', 'POST'])
@login_required
def market_page():
    sell_form = SellItemForm()
    buy_form = BuyItemForm()

    if request.method == "POST" and buy_form.validate_on_submit():
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object :
            # print(f"Purchased item: {purchased_item}")
            p_item_object.assign_ownership(current_user)
            flash(f"You have purchased {purchased_item}! for {p_item_object.price}", category='success')
        else:
            flash(f"Insufficient budget to purchase {p_item_object.name}.", category='danger')
        return redirect(url_for('market_page'))

    items = Item.query.filter_by(owner=None).all()
    owned_items = Item.query.filter_by(owner=current_user.id).all()
    return render_template("market.html",items = items, buy_form= buy_form, owned_items = owned_items)

@app.route("/register", methods = ['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email = form.email.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user=user_to_create)
        flash(f"Success! You're logged in as {user_to_create.username}",category='success')


        return redirect(url_for('market_page'))
    if form.errors != {}:                                   #If there are not any errors from the validations
        for error_msg in form.errors.values():
            flash(f"There was an error with creating account: {error_msg}",category='danger')
    return render_template('register.html', form = form)

@app.route("/login",methods = ['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password = form.password.data):
            login_user(user=attempted_user)
            flash(f"Success! You're logged in as {attempted_user.username}",category='success')
            return redirect(url_for('market_page'))
        else:
            flash(f"Username and password do not match! Please try again",category='danger')


    return render_template('login.html', form = form)
    

@app.route("/logout")
def logout_page():
    logout_user()
    flash(f"You have been logged out!",category='info')
    return redirect(url_for('home'))