import sys
sys.path.append('F:/e_commerce')
from e_commerce.app import app
from e_commerce.db import db
from flask_migrate import Migrate

migrate=Migrate(app,db)


if __name__ == '__main__':      
    with app.app_context(): 
        db.create_all()
        app.run(debug=True)
        