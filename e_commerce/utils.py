import jwt
from e_commerce.app import app
from flask import jsonify,request
from functools import wraps


def address_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            raw_token = token.split(" ")
        if not token:
            return jsonify({"status" : "error" , 
                            "message" : "token missing",
                            "code" : 901 ,
                            "data" : None})
        try:
            token = jwt.decode(raw_token[1], app.config['ADMIN_SECRET_KEY'] , algorithms='HS256')
        except:
            return jsonify({"status" : "error" , 
                            "code" : 902 ,
                            "message" : "invalid token" , 
                            "data" : None})
        return f( *args, **kwargs)
    return decorated