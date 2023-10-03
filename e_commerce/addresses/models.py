from e_commerce.db import db
from sqlalchemy import ForeignKey


class Addresses(db.Model): 
    __tablename__ = 'addresses' 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,ForeignKey('users.user_id'))
    street_address= db.Column(db.String(100))
    city= db.Column(db.String(100))
    state= db.Column(db.String(100))
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String(100))
    is_default= db.Column(db.Boolean)
    """
    
    def __init__(self,user_id,street_address,city,state,postal_code, country,is_default):
        self.user_id=user_id
        self.street_address=street_address
        self.city=city
        self.sate=state
        self.postal_code=postal_code
        self.country=country
        self.is_default=is_default
    """
class ShippingAddresses(db.Model): 
    __tablename__ = 'shipping_addresses' 
    address_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,ForeignKey('users.user_id'))
    street_address= db.Column(db.String(100))
    city= db.Column(db.String(100))
    state= db.Column(db.String(100))
    postal_code= db.Column(db.Integer)
    country= db.Column(db.String(100)) 
    
"""
    def __init__(self,street_address,city,state,postal_code, country):
        self.street_address=street_address
        self.city=city
        self.sate=state
        self.postal_code=postal_code
        self.country=country
        
"""
    