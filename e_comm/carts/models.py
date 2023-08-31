from db import db
class carts(db.Model):
    cart_id =db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.Integer,foreign_key=True('user.user_id'))
    creation_date=db.Column(db.DateTime)
    
class cart_items(db.Model):
    cart_item_id=db.Column(db.Integer,primary_key=True)
    cart_id=db.Column(db.Integer,foreign_key=True('cart_table.cart_id'))
    product_id=db.Column(db.Integer,foreign_key=True('product.product_id.user_id'))
    quantity=db.Column(db.Integer)
    