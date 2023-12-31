from e_commerce.db import db
#from e_commerce.app import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Payments(db.Model):
    __tablename__ = 'payments' 
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey('orders.order_id'), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(100), nullable=False)
    payment_method=db.Column(db.String(100))
    
class PaymentMethods(db.Model):
    __tablename__ = 'payment_methods' 
    payment_method_id=	db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,ForeignKey('users.user_id'), nullable=False)
    card_number=db.Column(db.String(100))
    expiration_date=db.Column(db.String(100))
    cvv=db.Column(db.String(100))
    
class Transactions(db.Model):
    __tablename__ = 'transactions' 
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)
    transaction_amount =db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(100), nullable=False)
    