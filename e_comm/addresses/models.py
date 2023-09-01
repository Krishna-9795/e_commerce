from db import db

class Addresses(db.Model): 
    __tablename__ = 'addresses' 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,db.Foreign_Key('user.user_id'))
    street_address= db.Column(db.String)
    city= db.Column(db.String)
    state= db.Column(db.String)
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String)
    is_default= db.Column(db.Boolean)
    
class ShippingAddresses(db.Model): 
    __tablename__ = 'shipping_addresses' 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,db.Foreign_Key('user.user_id'))
    street_address= db.Column(db.String)
    city= db.Column(db.String)
    state= db.Column(db.String)
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String) 
    