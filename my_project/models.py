from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()


class user(db.Model):
    user_id = db.Column(db.Integer , primary_key =True )
    name = db.Column(db.String(80) , nullable= False)
    email = db.Column(db.String(80) , nullable= False, unique = True)
    password = db.Column(db.String(80))
    wallet_balance = db.Column(db.Integer)
    created_on = db.Column(db.DateTime , default= datetime.utcnow)
    phone = db.Column(db.BigInteger)
    status = db.Column(db.Boolean , default = True)
    
class product(db.Model):
    product_id=db.Column(db.Integer , primary_key =True )
    name= db.Column(db.String(80) , nullable= False)
    description=db.Column(db.String(80))
    price=db.Column(db.Float, nullable=False)
    stock_quantity=db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey('categories.category_id'), nullable=False)
    
class category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class order_table(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

class OrderItem(db.Model):
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    
class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey('orders.order_id'), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.Boolean, nullable=False)
    
class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, ForeignKey('products.product_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.String)