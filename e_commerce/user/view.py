from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from e_commerce.user.models import Users
from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import datetime
#from e_commerce.app import db
from  e_commerce.db import db 
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = Users(username=data['username'], first_name=data['first_name'], last_name=data['last_name'],
                                        email=data['email'], password=hashed_password, wallet_balance=0,
                                        phone=data['phone'], country=data['country'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

#login 
def login():
    auth = request.get_json()
    
    user = Users.query.filter_by(email=auth['email']).first()

    if not user or not check_password_hash(user.password, auth['password']):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    
    user.last_login_date = datetime.utcnow()        # Update last login date
    db.session.commit()
    access_token = create_access_token(identity=user.user_id)
    return jsonify({'access_token': access_token},{'message': 'Login successful!', 'user_id': user.user_id}), 200

def get_user(user_id):
    user = Users.query.get(user_id)
    user_data=[]
    if user is None:
        return jsonify({'message': 'User not found'}),404
    else :
        user_data.append({
            'user_id': user.user_id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'wallet_balance': user.wallet_balance,
            'registration_date': user.registration_date,
            'phone': user.phone,
            'country': user.country,
            'last_login_date': user.last_login_date        
        })
    return jsonify({'user': user_data}),200


def get_all_users():
    users = Users.query.all()
    user_list =[]
    for user in users:
        user_list.append({
            'user_id': user.user_id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'wallet_balance': user.wallet_balance,
            'registration_date': user.registration_date,
            'phone': user.phone,
            'country': user.country,
            'last_login_date': user.last_login_date
        })
    return jsonify({'users': user_list})

def update_user(user_id):
    data = request.get_json()
    user = Users.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'})

    user.username = data.get('username', user.username)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.phone = data.get('phone', user.phone)
    user.country = data.get('country', user.country)
    db.session.commit()

    return jsonify({'message': 'User updated successfully'})

# Delete
def delete_user(user_id):
    
    user = Users.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'})