from e_comm.app import db

class Orders(db.Model):
    __tablename__ = 'orders' 
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    order_status= db.Column(db.String)
    shipping_address=db.Column(db.String)
    payment_method=db.Column(db.String)
    coupon_id=db.Column(db.Integer,db.ForeignKey('Coupon.coupon_id'),nullable=True)

class OrderItems(db.Model):
    __tablename__ = 'orders_items' 
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    discount_percentage=db.Column(db.Float)
    total_amount= db.Column(db.Float, nullable=False)
    
