
#from e_commerce.utils import admin_token
from e_commerce.admin import view
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin/login' , methods = ['POST'])
def admin_login():
    return view.admin_login()