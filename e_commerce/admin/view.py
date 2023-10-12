from e_commerce.admin.models import Admin
from e_commerce.db import db
from e_commerce.app import app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request , jsonify
import jwt
from flask_bcrypt import Bcrypt  # Import bcrypt from Flask-Bcrypt
from flask_jwt_extended import create_access_token
bcrypt = Bcrypt(app)

def admin_register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_admin = Admin(admin_name=data['admin_name'],email=data['email'], password=hashed_password)
    db.session.add(new_admin)
    db.session.commit()

    return jsonify({'message': 'New admin created!'})



def admin_login():
    if request.method == 'POST':
        credentials = request.json
        email = credentials['email']
        password = credentials['password']
        data = Admin.query.filter_by(email=email).first()
        
        if data:
            # Use bcrypt to check if the user-provided password matches the stored hashed password
            if bcrypt.check_password_hash(data.password, password):
                # Passwords match, proceed with authentication
                try:
                    admin_data = {'id': data.id,
                                    'name': data.admin_name,
                                    'email': data.email}
                    token_data = {'id': data.id}
                    token = jwt.encode(token_data, app.config['ADMIN_SECRET_KEY'], algorithm='HS256')

                    return jsonify({
                        "status": "success",
                        "code": "900",
                        "token": token,
                        "message": "successfully logged in",
                        "data": admin_data
                    })
                except:
                    return jsonify({
                        "status": "error",
                        "code": "901",
                        "message": "invalid id or password",
                        "data": None
                    })
            return jsonify({
                "status": "error",
                "code": "901",
                "message": "invalid id or password",
                "data": None
            })

    return jsonify({
        "status": "error",
        "code": "901",
        "message": "invalid id or password",
        "data": None
    })


def get_admin(id):
    adm=Admin.query.get(id)
    if  adm :
        return jsonify({'id' : adm.id ,
                        'name' : adm.admin_name,
                        'email' : adm.email,
                        'created_on':adm.created_on }) 
    else :
        return jsonify({'message': 'admin not found'})


def update_admin(id):
    data = request.get_json()
    admin = Admin.query.get(id)
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    if not admin:
        return jsonify({'message': 'User not found'})
    admin.admin_name=data.get('name',admin.admin_name)
    admin.email=data.get('email',admin.email)
    admin.password=hashed_password
    
    db.session.commit()
    return jsonify({'message': 'Admin updated successfully'
                    })

# Delete
def delete_admin(id):
    
    admin = Admin.query.get(id)
    if not admin:
        return jsonify({'message': 'admin not found'})

    db.session.delete(admin)
    db.session.commit()

    return jsonify({'message': 'admin deleted successfully'})