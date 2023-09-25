from e_commerce.app import app
from e_commerce.utils import admin_token
from e_commerce.admin import view



@app.route('/admin/login' , methods = ['POST'])
def admin_login():
    return view.admin_login()