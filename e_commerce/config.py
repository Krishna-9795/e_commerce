from e_commerce.app import app
from datetime import timedelta

class credentials:
        app.config['SECRET_KEY'] = 'ecommerce123'
        app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
        
        app.config['JSON_SORT_KEYS'] = False  
        app.config['ADMIN_SECRET_KEY'] = 'i am an admin'
        app.config['USER_SECRET_KEY'] = 'i am a user'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False