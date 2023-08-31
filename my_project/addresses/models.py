from db import db

class addresses(db.Model): 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,Foreign_Key=True('user.user_id'))
    street_address= db.Column(db.String)
    city= db.Column(db.String)
    state= db.Column(db.String)
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String)
    is_default= db.Column(db.Boolean)
    
class shipping_addresses(db.Model): 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,Foreign_Key=True('user.user_id'))
    street_address= db.Column(db.String)
    city= db.Column(db.String)
    state= db.Column(db.String)
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String) 
    