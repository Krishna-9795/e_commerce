from e_commerce.db import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Products(db.Model):
    __tablename__ = 'products' 
    product_id=db.Column(db.Integer , primary_key =True )
    name= db.Column(db.String(80) , nullable= False)
    description=db.Column(db.String(80))
    price=db.Column(db.Float, nullable=False)
    stock_quantity=db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey('categories.category_id'), nullable=False)
    image_url=db.Column(db.String(100),nullable=False)
    manufacturer_id = db.Column(db.Integer, ForeignKey('manufacturers.manufacturer_id'))
    creation_date=db.Column(db.String(80))
    average_rating = db.Column(db.Float)
    total_ratings = db.Column(db.Integer)
    
    
class ProductVariants(db.Model):
    __tablename__ = 'product_variants' 
    variant_id=	db.Column(db.Integer, primary_key=True)
    product_id= db.Column(db.Integer, ForeignKey('products.product_id'), nullable=False)
    color=db.Column(db.String(100))
    size=db.Column(db.String(100))
    material= db.Column(db.String(100))
    other_features=db.Column(db.String(100))
    specification=db.Column(db.String(100))
    image_url=db.Column(db.String(100))
    price=	db.Column(db.Float)
    quantity=db.Column(db.Float)
    created_at=db.Column(db.DateTime, default= datetime.utcnow)
    
    
class Categories(db.Model):
    __tablename__ = 'categories' 
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
class  Manufacturers(db.Model):
    __tablename__ = 'manufacturers' 
    manufacturer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country= db.Column(db.String(100))
    