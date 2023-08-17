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
    
class product(db.model):
    product_id=db.Column(db.Integer , primary_key =True )
    name= db.Column(db.String(80) , nullable= False)
    description=db.Column(db.String(80))
    price=db.Column(db.Float, nullable=False)
    stock_quantity=db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey('categories.category_id'), nullable=False)
    
class category(db.model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class order_table(db.model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

