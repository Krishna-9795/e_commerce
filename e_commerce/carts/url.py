from e_commerce.app import app
from e_commerce.carts import view
from flask import Blueprint


cart_bp = Blueprint('carts', __name__)
    

# Create a Cart
@cart_bp.route('/carts/register', methods=['POST'])
def create_carts():
    return view.create_cart()

# Retrieve a Cart by ID
@cart_bp.route('/carts/retrieve/<int:cart_id>', methods=['GET'])
def get_carts():
    return view.get_cart()

# Update a Cart by ID
@cart_bp.route('/carts/update/<int:cart_id>', methods=['PUT'])
def update_carts():
    return view.update_cart()

# Delete a Cart by ID
@cart_bp.route('/carts/delete/<int:cart_id>', methods=['DELETE'])
def delete_carts():
    return view.delete_cart()

# Create a Cart Item
@cart_bp.route('/carts/cart_items/register', methods=['POST'])
def create_cart_items():
    return view.create_cart_item()

# Retrieve a Cart Item by ID
@cart_bp.route('/carts/cart_items/retrieve/<int:cart_item_id>', methods=['GET'])
def get_cart_items():
    return view.get_cart_item()

# Update a Cart Item by ID
@cart_bp.route('/carts/cart_items/update/<int:cart_item_id>', methods=['PUT'])
def update_cart_items():
    return view.update_cart_item()

# Delete a Cart Item by ID
@cart_bp.route('/carts/cart_items/delete/<int:cart_item_id>', methods=['DELETE'])
def delete_cart_item():
    return view.delete_cart_item()