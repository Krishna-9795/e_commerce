from e_commerce.carts import view
from flask import Blueprint


cart_bp = Blueprint('carts', __name__)


# Create a Cart
@cart_bp.route('/carts/create', methods=['POST'])
def create_carts():
    return view.create_cart()

# Retrieve a Cart by ID
@cart_bp.route('/carts/retrieve/<int:cart_id>', methods=['GET'])
def get_carts(cart_id):
    return view.get_cart(cart_id)

# Update a Cart by ID
@cart_bp.route('/carts/update/<int:cart_id>', methods=['PUT'])
def update_carts(cart_id):
    return view.update_cart(cart_id)

# Delete a Cart by ID
@cart_bp.route('/carts/delete/<int:cart_id>', methods=['DELETE'])
def delete_carts(cart_id):
    return view.delete_cart(cart_id)

# Create a Cart Item
@cart_bp.route('/carts/cart_items/create', methods=['POST'])
def create_cart_items():
    return view.create_cart_item()

# Retrieve a Cart Item by ID
@cart_bp.route('/carts/cart_items/retrieve/<int:cart_item_id>', methods=['GET'])
def get_cart_items(cart_item_id):
    return view.get_cart_item(cart_item_id)

# Update a Cart Item by ID
@cart_bp.route('/carts/cart_items/update/<int:cart_item_id>', methods=['PUT'])
def update_cart_items(cart_item_id):
    return view.update_cart_item(cart_item_id)

# Delete a Cart Item by ID
@cart_bp.route('/carts/cart_items/delete/<int:cart_item_id>', methods=['DELETE'])
def delete_cart_item(cart_item_id):
    return view.delete_cart_item(cart_item_id)