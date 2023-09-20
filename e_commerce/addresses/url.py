from e_commerce.app import app
from flask_jwt_extended import jwt_required
from e_commerce.addresses.view import address_data, update_address, delete_address, shipping_address_data, update_shipping_address, delete_shipping_address



@app.route('/addresses',methods=['POST'])
#@jwt_required()
def addresses_data():
    return address_data()
    
@app.route('/update/<int:address_id>',methods=['PUT']) 
# @jwt_required()
def update_addresses():
    return update_address()
# Delete
@app.route('/delete/<int:address_id>', methods=['DELETE'])
# @jwt_required()
def delete_addresses():
    return delete_address()

@app.route('/shipping_addresses',methods=['POST'])
#  @jwt_required()
def ship_addresses_data():
    return shipping_address_data()

@app.route('/shipping_address/update/<int:address_id>',methods=['PUT']) 
#   @jwt_required()
def update_ship_addresses():
    return update_shipping_address()

@app.route('/shipping_address/delete/<int:address_id>', methods=['DELETE'])
#  @jwt_required()
def delete_shipping_addresses():
    return delete_shipping_address()
