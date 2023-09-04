from db import db
from datetime import datetime
class Users(db.Model):
    __tablename__ = 'users' 
    user_id = db.Column(db.Integer , primary_key =True ,unique=True)
    username=db.Column(db.String(80),nullable=False)
    first_name = db.Column(db.String(80) , nullable= False)
    last_name = db.Column(db.String(80) , nullable= False)
    email = db.Column(db.String(80) , nullable= False, unique = True)
    password = db.Column(db.String(200))
    wallet_balance = db.Column(db.Integer)
    registration_date = db.Column(db.DateTime , default= datetime.utcnow)
    phone = db.Column(db.BigInteger)
    country=db.Column(db.String(80) ,nullable=False)
    last_login_date=db.Column(db.DateTime)

    def __init__(self,username,first_name, last_name,email,password,wallet_balance,
                phone, country):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email=email
        self.password=password
        self.wallet_balance=wallet_balance
        self.phone = phone
        self.country=country
    