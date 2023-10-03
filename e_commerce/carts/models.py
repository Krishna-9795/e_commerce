from sqlalchemy import ForeignKey
#from e_commerce.app import db
from e_commerce.db import db
class Carts(db.Model):
    __tablename__ = 'carts' 
    cart_id =db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.Integer,ForeignKey('users.user_id'))
    creation_date=db.Column(db.DateTime)

class Cart_items(db.Model):
    __tablename__ = 'cart_items'  # Specify the desired table name
    cart_item_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, ForeignKey('carts.cart_id'))
    product_id = db.Column(db.Integer, ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer)
    
