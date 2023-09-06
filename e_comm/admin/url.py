from e_comm.app import app
from flask_jwt_extended import jwt_required
from admin.view import register,login,get_all_users,update_user

def app_routes(app):
    #registering
    @app.route('/register', methods=['POST'])
    def registers():
            return register()
        #login
    @app.route('/login', methods=['POST'])
    def login_routes():
        return login()
    #getting the list of users
    @app.route('/users', methods=['GET'])
    @jwt_required()
    def get_all_users_route():
        return get_all_users()


    #update
    @app.route('/update/<int:user_id>', methods=['PUT'])
    @jwt_required()
    def update_user_route():
        return update_user()