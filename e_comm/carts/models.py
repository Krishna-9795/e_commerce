from e_comm.app import db
from flask_sqlalchemy import ForeignKey
class Carts(db.Model):
    __tablename__ = 'carts' 
    cart_id =db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.Integer,ForeignKey('user.user_id'))
    creation_date=db.Column(db.DateTime)

class Cart_items(db.Model):
    __tablename__ = 'cart_items'  # Specify the desired table name
    cart_item_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, ForeignKey('cart_table.cart_id'))
    product_id = db.Column(db.Integer, ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer)
    
