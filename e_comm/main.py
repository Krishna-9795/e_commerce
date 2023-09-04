from flask import Flask
from flask_jwt_extended import JWTManager

from datetime import timedelta
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:krishna123@localhost/ecommerce'
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)


jwt=JWTManager(app)

db.init_app(app)

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
