from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta 
from flask_migrate import Migrate
import sys
sys.path.append('F:/e_commerce')




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:krishna123@localhost/ecommerce'
app.config['SECRET_KEY'] = 'ecommerce123'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

db=SQLAlchemy(app)
jwt=JWTManager(app)

migrate=Migrate(app,db)

#db.init_app(app)

with app.app_context():    
    db.create_all()

from e_comm.admin.url import admin_routes
from e_comm.addresses.url import address_routes
from e_comm.carts.url import cart_routes
from e_comm.coupons.url import coupon_routes
from e_comm.orders.url import order_routes
from e_comm.payments.url import payment_routes
from e_comm.product.url import product_routes
from e_comm.review.url import review_routes

admin_routes(app)
address_routes(app)
cart_routes(app)
coupon_routes(app)
order_routes(app)
payment_routes(app)
product_routes(app)
review_routes(app)

    



