from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

from e_comm.app import init_app

app = init_app()

    
if __name__ == '__main__':
    app.run(debug=True)
