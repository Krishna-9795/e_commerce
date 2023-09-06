from e_comm.app import app
from flask_jwt_extended import jwt_required
from admin.view import register,login,get_all_users,update_user,delete_user,get_user

def app_routes(app):
    # Registering
    @app.route('/register', methods=['POST'])
    def registers():
            return register()
    # login
    @app.route('/login', methods=['POST'])
    def login_routes():
        return login()
    
    # Getting the user details according to user_id
    @app.route('/users/<int:user_id>', methods=['GET'])
    @jwt_required()
    def get_user_route(user_id):
        return get_user(user_id)
    
    # Getting the list of users
    @app.route('/users', methods=['GET'])
    @jwt_required()
    def get_all_users_route():
        return get_all_users()


    # Update
    @app.route('/update/<int:user_id>', methods=['PUT'])
    @jwt_required()
    def update_user_route():
        return update_user()
    # Delete
    @app.route('/delete/<int:user_id>', methods=['DELETE'])
    @jwt_required()
    def delete_user_route():
        return delete_user()
    