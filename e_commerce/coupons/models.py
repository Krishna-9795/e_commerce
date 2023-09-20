from e_commerce.app import db


class Coupons(db.Model):
    __tablename__ = 'coupons' 
    coupon_id= db.Column(db.Integer, primary_key=True)
    code=db.Column(db.String, unique=True, nullable=False)
    coupon_amount= db.Column(db.Float, nullable=False)
    coupon_expiration_date= db.Column(db.DateTime)
    