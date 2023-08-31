from db import db

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
    
class coupons(db.Model):
    coupon_id= db.Column(db.Integer, primary_key=True)
    code=db.Column(db.String, unique=True, nullable=False)
    coupon_amount= db.Column(db.Float, nullable=False)
    coupon_expiration_date= db.Column(db.DateTime)