from db import db
from datetime import datetime
class users(db.Model):
    user_id = db.Column(db.Integer , primary_key =True ,unique=True)
    username=db.Column(db.String(80),nullable=False)
    first_name = db.Column(db.String(80) , nullable= False)
    last_name = db.Column(db.String(80) , nullable= False)
    email = db.Column(db.String(80) , nullable= False, unique = True)
    password = db.Column(db.String(80))
    wallet_balance = db.Column(db.Integer)
    registration_date = db.Column(db.DateTime , default= datetime.utcnow)
    phone = db.Column(db.BigInteger)
    country=db.Column(db.String ,nullable=False)
    last_login_date=db.Column(db.Datetime)
