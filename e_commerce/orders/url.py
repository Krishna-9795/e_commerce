from e_commerce.app import app
from e_commerce.orders import view
from flask import Blueprint

order_bp = Blueprint('orders', __name__)
    

# Create an Order 
@order_bp.route('/orders/register', methods=['POST'])
def create_orders():
    return view.create_order()

#Return an order by id
@order_bp.route('/orders/retrieve/<int:order_id>', methods=['GET'])
def get_orders():
    return view.get_order()

# Update an order 
@order_bp.route('/orders/update/<int:order_id>', methods=['PUT'])
def update_orders():
    return view.update_order()

# Delete an Order by ID
@order_bp.route('/orders/delete/<int:order_id>', methods=['DELETE'])
def delete_orders():
    return view.delete_order()

# Create an Order Item
@order_bp.route('/orders/order-items/register', methods=['POST'])
def create_order_items():
    return view.create_order_item()

# Retrieve an Order Item by ID
@order_bp.route('/orders/order-items/retrieve/<int:order_item_id>', methods=['GET'])
def get_order_item():
    return view.get_order_item()

# Update an Order Item by ID
@order_bp.route('/orders/order-items/<int:order_item_id>', methods=['PUT'])
def update_order_item():
    return view.update_order_item()

# Delete an Order Item by ID
@order_bp.route('/orders/order-items/<int:order_item_id>', methods=['DELETE'])
def delete_order_item():
    return view.delete_order_item()