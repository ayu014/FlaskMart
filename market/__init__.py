import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

load_dotenv()

secret_key  = os.environ.get("SECRET_KEY")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



from market import routes