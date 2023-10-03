from e_commerce.db import db
#from e_commerce.app import db
from sqlalchemy import ForeignKey

class Reviews(db.Model):
    __tablename__ = 'reviews' 
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'))
    product_id = db.Column(db.Integer, ForeignKey('products.product_id'))
    rating = db.Column(db.Float, nullable=False)
    review_text = db.Column(db.String(100))
    review_date = db.Column(db.DateTime)
    