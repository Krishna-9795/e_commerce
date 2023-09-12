from e_comm.app import db

class  Manufacturers(db.Model):
    __tablename__ = 'manufacturers' 
    manufacturer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country= db.Column(db.String)