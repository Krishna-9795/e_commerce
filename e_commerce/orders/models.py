from e_commerce.db import db
#from e_commerce.app import db
from sqlalchemy import ForeignKey

class Orders(db.Model):
    __tablename__ = 'orders' 
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    order_status= db.Column(db.String(100))
    shipping_address=db.Column(db.String(100))
    payment_method=db.Column(db.String(100))
    coupon_id=db.Column(db.Integer, ForeignKey('coupons.coupon_id'),nullable=True)

class OrderItems(db.Model):
    __tablename__ = 'orders_items' 
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, ForeignKey('products.product_id'), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    discount_percentage=db.Column(db.Float)
    total_amount= db.Column(db.Float, nullable=False)
    
