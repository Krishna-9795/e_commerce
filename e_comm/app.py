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
#db.init_app(app)
with app.app_context():    
    db.create_all()
from e_comm.admin.url import app_routes
from e_comm.addresses.url import address_routes
app_routes(app)
address_routes(app)
