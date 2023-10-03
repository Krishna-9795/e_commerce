import jwt
from e_commerce.app import app
from flask import jsonify,request
from functools import wraps
import smtplib
import random


def admin_token(f):
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


def user_otp(receiver_mail):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("test.developer.off@gmail.com", "fpyetsdbwevindcw")
    otp = random.randint(100000, 999999)
    otp = str(otp)
    msg='Hello, Your OTP is '+str(otp)
    s.sendmail("test.developer.off@gmail.com", receiver_mail, msg)
    s.quit()
    return(otp)