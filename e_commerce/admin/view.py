from e_commerce.admin.models import Admin
from e_commerce.product.models import Products
from e_commerce.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import e_commerce.config as server
from flask import request , jsonify
import jwt

def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_admin = Admin(admin_name=data['admin_name'],email=data['email'], password=hashed_password)
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({'message': 'New admin created!'})



def admin_login(): 
    from e_commerce.app import app        
    if request.method == 'POST':
        credentials = request.json
        email = credentials['email']
        password = credentials['password']
        data = Admin.query.filter_by(email = email).first()
        try:
            admin_data = {'id' : data.id ,
                        'name' : data.admin_name,
                        'email' : data.email}
            token_data = {'id' : data.id}
            token = jwt.encode(token_data , app.config['ADMIN_SECRET_KEY'] , algorithm= 'HS256')
            if data.password == password :
                return jsonify({"status" : "success" , 
                                "code" : "900" , 
                                "token" : token ,
                                "message" : "successfully logged in" ,
                                "data" : admin_data})
        except:
            return({"status" : "error" , 
                "code" : "901" , 
                "message" : "invalid id or password" ,
                "data" : None})
    return({"status" : "error" , 
            "code" : "901" , 
            "message" : "invalid id or password" ,
            "data" : None})
    

