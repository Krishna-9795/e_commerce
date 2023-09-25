from flask_jwt_extended import jwt_required
from e_commerce.addresses.view import address_data, update_address, delete_address, shipping_address_data, update_shipping_address, delete_shipping_address

from flask import Blueprint

address_bp = Blueprint('address', __name__)


@address_bp.route('/address/register',methods=['POST'])
#@jwt_required()
def addresses_data():
    return address_data()
    
@address_bp.route('/address/update/<int:address_id>',methods=['PUT']) 
# @jwt_required()
def update_addresses():
    return update_address()
# Delete
@address_bp.route('/address/delete/<int:address_id>', methods=['DELETE'])
# @jwt_required()
def delete_addresses():
    return delete_address()

@address_bp.route('/address/shipping_addresses',methods=['POST'])
#  @jwt_required()
def ship_addresses_data():
    return shipping_address_data()

@address_bp.route('/address/shipping_address/update/<int:address_id>',methods=['PUT']) 
#   @jwt_required()
def update_ship_addresses():
    return update_shipping_address()

@address_bp.route('/address/shipping_address/delete/<int:address_id>', methods=['DELETE'])
#  @jwt_required()
def delete_shipping_addresses():
    return delete_shipping_address()

