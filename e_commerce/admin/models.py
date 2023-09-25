from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from e_commerce.app import db
from e_commerce.db import db

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer , primary_key =True)
    admin_name = db.Column(db.String(45))
    password = db.Column(db.String(45))
    email = db.Column(db.String(45))
    created_on = db.Column(db.DateTime, default = datetime.utcnow)