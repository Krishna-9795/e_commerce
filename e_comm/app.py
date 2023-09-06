
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:krishna123@localhost/ecommerce'
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

db=SQLAlchemy(app)
jwt=JWTManager(app)

from e_comm.admin.url import app_routes
app_routes(app)


