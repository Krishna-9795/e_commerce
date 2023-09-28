from flask import Flask
from db import db
from flask_jwt_extended import JWTManager
from datetime import timedelta 
from flask_migrate import Migrate
import sys
sys.path.append('F:/e_commerce')
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:krishna123@localhost/ecommerce'
app.config['SECRET_KEY'] = 'ecommerce123'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

#db=SQLAlchemy(app)
jwt=JWTManager(app)

migrate=Migrate(app,db)
#db.init_app(app)    
with app.app_context(): 
        db.create_all()


from e_commerce.user.url import user_bp
from e_commerce.addresses.url import address_bp
from e_commerce.review.url import review_bp
from e_commerce.product.url import product_bp
from e_commerce.payments.url import payment_bp
from e_commerce.orders.url import order_bp
from e_commerce.coupons.url import coupon_bp
from e_commerce.carts.url import cart_bp
from e_commerce.admin.url import admin_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(address_bp, url_prefix='/address')
app.register_blueprint(review_bp, url_prefix='/reviews')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(payment_bp, url_prefix='/payments')
app.register_blueprint(order_bp, url_prefix='/orders')
app.register_blueprint(coupon_bp, url_prefix='/coupons')
app.register_blueprint(cart_bp, url_prefix='/carts')
app.register_blueprint(admin_bp, url_prefix='/admin')






