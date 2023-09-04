from e_comm.main import app
from flask_jwt_extended import jwt_required
from admin.view import register,login,get_all_users,update_user

#registering
@app.route('/register', methods=['POST'])
def register():
        return register()
    #login
@app.route('/login', methods=['POST'])
def login():
    return login()
#getting the list of users
@app.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    return get_all_users()


#update
@app.route('/update/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user():
    return update_user()