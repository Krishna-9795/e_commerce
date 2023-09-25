from e_commerce.admin.models import Admin

from e_commerce.app import app , db
#import config as server
from flask import request , jsonify
import jwt


def admin_login():    
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
