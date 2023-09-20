from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta 
from flask_migrate import Migrate
import sys
sys.path.append('F:/e_commerce')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:krishna123@localhost/ecommerce'
app.config['SECRET_KEY'] = 'ecommerce123'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

db=SQLAlchemy(app)
jwt=JWTManager(app)

#db.init_app(app)

import url 

migrate=Migrate(app,db)

if __name__ == '__main__':
    with app.app_context():    
        db.create_all()
    app.run(debug=True)




