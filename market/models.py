from market import bcrypt
from flask_login import UserMixin
from market import db,login_manager
from babel.numbers import format_currency

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key = True)
    username= db.Column(db.String(length = 12),nullable = False, unique = True)
    password_hash = db.Column(db.String(length = 60),nullable =False)
    email = db.Column(db.String(length = 50),nullable = False,unique = True)
    budget = db.Column(db.Integer, default = 1000)
    items = db.relationship('Item',backref='owned_user',lazy = True)


    @property
    def prettier_budget(self):
        return format_currency(self.budget,'INR', locale='en_IN',format=None)


    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(password=plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)
    
    def can_purchase(self,item_obj):
        return self.budget>=item_obj.price
    
    def can_sell(self,item_obj):
        return item_obj in self.items


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False)
    barcode = db.Column(db.String(length = 12), nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(length = 1024), nullable = False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item: {self.name}"
    
    def assign_ownership(self,user):
        self.owner = user.id                #p_item_object.owner = current_user.id                         
        user.budget -= self.price            #current_user.budget -= p_item_object.price 
        db.session.commit()

    def sell(self,user):
        self.owner = None
        user.budget += self.price
        db.session.commit()
    