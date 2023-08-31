from db import db
from datetime import datetime

class products(db.Model):
    product_id=db.Column(db.Integer , primary_key =True )
    name= db.Column(db.String(80) , nullable= False)
    description=db.Column(db.String(80))
    price=db.Column(db.Float, nullable=False)
    stock_quantity=db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey=True('categories.category_id'), nullable=False)
    image_url=db.Column(db.String,nullable=False)
    manufacturer_id = db.Column(db.Integer, ForeignKey=True('manufacturers.manufacturer_id'))
    creation_date=db.Column(db.String)
    average_rating = db.Column(db.Float)
    total_ratings = db.Column(db.Integer)
    
    
class product_variants():
    variant_id=	db.Column(db.Integer, primary_key=True)
    product_id= db.Column(db.Integer, ForeignKey=True('products.product_id'), nullable=False)
    color=db.Column(db.String)
    size=db.Column(db.Float)
    material= db.Column(db.String)
    other_features=db.Column(db.String)
    specification=db.Column(db.String)
    image_url=db.Column(db.String)
    price=	db.Column(db.Float)
    quantity=db.Column(db.Float)
    created_at=db.Column(db.DateTime, default= datetime.utcnow)
    
    
class categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
class  manufacturers(db.Model):
    manufacturer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country= db.Column(db.String)
    
class reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey=True('users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, ForeignKey=True('products.product_id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_text = db.Column(db.String)
    review_date = db.Column(db.DateTime)
