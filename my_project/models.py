from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()


class users(db.Model):
    user_id = db.Column(db.Integer , primary_key =True ,unique=True)
    username=db.Column(db.String(80),nullable=False)
    first_name = db.Column(db.String(80) , nullable= False)
    last_name = db.Column(db.String(80) , nullable= False)
    email = db.Column(db.String(80) , nullable= False, unique = True)
    password = db.Column(db.String(80))
    wallet_balance = db.Column(db.Integer)
    registration_date = db.Column(db.DateTime , default= datetime.utcnow)
    phone = db.Column(db.BigInteger)
    country=db.Column(db.String ,nullable=False)
    last_login_date=db.Column(db.Datetime)

class products(db.Model):
    product_id=db.Column(db.Integer , primary_key =True )
    name= db.Column(db.String(80) , nullable= False)
    description=db.Column(db.String(80))
    price=db.Column(db.Float, nullable=False)
    stock_quantity=db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey=True('categories.category_id'), nullable=False)
    image_url=db.Column(db.String,nullable=False)
    manufacturer_id = db.Column(db.Integer, ForeignKey=True('manufacturers.manufacturer_id'))
    creation_date=db.Column(db.String)
    average_rating = db.Column(db.Float)
    total_ratings = db.Column(db.Integer)
    
class categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
class  manufacturers(db.Model):
    manufacturer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country= db.Column(db.String)
    

class carts(db.Model):
    cart_id =db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.Integer,foreign_key=True('user.user_id'))
    creation_date=db.Column(db.DateTime)
    
class cart_items(db.Model):
    cart_item_id=db.Column(db.Integer,primary_key=True)
    cart_id=db.Column(db.Integer,foreign_key=True('cart_table.cart_id'))
    product_id=db.Column(db.Integer,foreign_key=True('product.product_id.user_id'))
    quantity=db.Column(db.Integer)
    

    
class orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey=True('users.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    order_status= db.Column(db.String)
    shipping_address=db.Column(db.String)
    payment_method=db.Column(db.String)
    coupon_id=db.Column(db.Integer,ForeignKey=True('Coupon.coupon_id'),nullable=True)

class order_items(db.Model):
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey=True('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, ForeignKey=True('products.product_id'), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    discount_percentage=db.Column(db.Float)
    total_amount= db.Column(db.Float, nullable=False)
class payments(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey=True('orders.order_id'), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String, nullable=False)
    payment_method=db.Column(db.String)
    
class payment_methods(db.Model):
    payment_method_id=	db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, ForeignKey=True('users.user_id'), nullable=False)
    card_number=db.Column(db.String)
    expiration_date=db.Column(db.String)
    cvv=db.Column(db.String)

class product_variants():
    variant_id=	db.Column(db.Integer, primary_key=True)
    product_id= db.Column(db.Integer, ForeignKey=True('products.product_id'), nullable=False)
    color=db.Column(db.String)
    size=db.Column(db.Float)
    material= db.Column(db.String)
    other_features=db.Column(db.String)
    specification=db.Column(db.String)
    image_url=db.Column(db.String)
    price=	db.Column(db.Float)
    quantity=db.Column(db.Float)
    created_at=db.Column(db.DateTime, default= datetime.utcnow)

	
class reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey=True('users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, ForeignKey=True('products.product_id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_text = db.Column(db.String)
    review_date = db.Column(db.DateTime)

class addresses(db.Model): 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,Foreign_Key=True('user.user_id'))
    street_address= db.Column(db.String)
    city= db.Column(db.String)
    state= db.Column(db.String)
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String)
    is_default= db.Column(db.Boolean)
    
class shipping_addresses(db.Model): 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,Foreign_Key=True('user.user_id'))
    street_address= db.Column(db.String)
    city= db.Column(db.String)
    state= db.Column(db.String)
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String) 
    
class coupons(db.Model):
    coupon_id= db.Column(db.Integer, primary_key=True)
    code=db.Column(db.String, unique=True, nullable=False)
    coupon_amount= db.Column(db.Float, nullable=False)
    coupon_expiration_date= db.Column(db.DateTime)
    
class transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey=True('user.user_id'), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)
    transaction_amount =db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String, nullable=False)
    
    

