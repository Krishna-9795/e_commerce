import jwt
import os
import uuid
from werkzeug.utils import secure_filename 
from datetime import datetime
from flask import jsonify,request
from functools import wraps


def admin_token(f):
    from e_commerce.app import app
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




def user_token(f):
    from e_commerce.app import app
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
            token = jwt.decode(raw_token[1], app.config['USER_SECRET_KEY'] , algorithms='HS256')
        except:
            return jsonify({"status" : "error" , 
                            "code" : 902 ,
                            "message" : "invalid token" , 
                            "data" : None})
        return f( *args, **kwargs)
    return decorated

from e_commerce.app import app
import os


def generate_unique_filename(filename):
    unique_id = str(uuid.uuid4().hex)
    _, extension = os.path.splitext(filename)
    unique_filename = f"{unique_id}{extension}"
    return unique_filename

def upload_image():
    try:
        # Check if a file is included in the request
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided."}), 400

        file = request.files['image']

        # Check if the file is empty
        if file.filename == '':
            return jsonify({"error": "No selected file."}), 400

        # Generate a unique filename
        unique_filename = generate_unique_filename(file.filename)

        # Save the uploaded file with the unique filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)

        return jsonify({"message": "Image uploaded successfully", "file_path": file_path}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


"""
import smtplib
import random
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
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
"""





