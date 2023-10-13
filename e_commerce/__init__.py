from e_commerce.app import app
from datetime import timedelta
import sys
sys.path.append('F:/e_commerce')
import os
from flask_jwt_extended import JWTManager

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:krishna123@localhost/ecommerce'
app.config['SECRET_KEY'] = 'ecommerce123'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['ADMIN_SECRET_KEY'] = 'i am an admin'
app.config['USER_SECRET_KEY'] = 'i am a user'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
UPLOAD_FOLDER = 'uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.app_context().push()
jwt=JWTManager(app)



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



