from flask_jwt_extended import jwt_required
from e_commerce.user.view import register,login,get_all_users,update_user,delete_user,get_user
from flask import Blueprint

user_bp = Blueprint('user', __name__)

# Registering
@user_bp.route('/user/register', methods=['POST'])
def registers():
        return register()
# login
@user_bp.route('/user/login', methods=['POST'])
def login_routes():
    return login()

# Getting the user details according to user_id
@user_bp.route('/user/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_route(user_id):
    return get_user(user_id)

# Getting the list of users
@user_bp.route('/user/user_retrieval', methods=['GET'])
@jwt_required()
def get_all_users_route():
    return get_all_users()


# Update
@user_bp.route('user/update/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_route(user_id):
    return update_user(user_id)
# Delete
@user_bp.route('user/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_route(user_id):
    return delete_user(user_id)
