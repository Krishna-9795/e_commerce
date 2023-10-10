from flask_jwt_extended import jwt_required
from e_commerce.addresses import view

from flask import Blueprint

address_bp = Blueprint('address', __name__)


@address_bp.route('/address/register',methods=['POST'])
#@jwt_required()
def addresses_data():
    return view.address_data()
    
@address_bp.route('/address/update/<int:address_id>',methods=['PUT']) 
# @jwt_required()
def update_addresses(address_id):
    return view.update_address(address_id)

# Retrieve address
@address_bp.route('/address/get/<int:address_id>',methods=['get'])
def gets_address(address_id):
    return view.get_address(address_id) 

# Delete
@address_bp.route('/address/delete/<int:address_id>', methods=['DELETE'])
# @jwt_required()
def delete_addresses(address_id):
    return view.delete_address(address_id)

# Creating a shippping address
@address_bp.route('/address/shipping_addresses',methods=['POST'])
#  @jwt_required()
def ship_addresses_data():
    return view.shipping_address_data()

# Retrieving a shipping address
@address_bp.route('/shipping_address/get/<int:address_id>',methods=['get'])
def gets_ship_address(address_id):
    return view.get_ship_address(address_id) 


# Updating a shipping address
@address_bp.route('/address/shipping_address/update/<int:address_id>',methods=['PUT']) 
#   @jwt_required()
def update_ship_addresses(address_id):
    return view.update_shipping_address(address_id)

# Deleting a shipping address
@address_bp.route('/address/shipping_address/delete/<int:address_id>', methods=['DELETE'])
#  @jwt_required()
def delete_shipping_addresses(address_id):
    return view.delete_shipping_address(address_id)

