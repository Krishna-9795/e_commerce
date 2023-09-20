from e_commerce.app import app
from e_commerce.orders import view
    

# Create an Order 
@app.route('/orders', methods=['POST'])
def create_orders():
    return view.create_order()

#Return an order by id
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_orders():
    return view.get_order()

# Update an order 
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_orders():
    return view.update_order()

# Delete an Order by ID
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_orders():
    return view.delete_order()

# Create an Order Item
@app.route('/order-items', methods=['POST'])
def create_order_items():
    return view.create_order_item()

# Retrieve an Order Item by ID
@app.route('/order-items/<int:order_item_id>', methods=['GET'])
def get_order_item():
    return view.get_order_item()

# Update an Order Item by ID
@app.route('/order-items/<int:order_item_id>', methods=['PUT'])
def update_order_item():
    return view.update_order_item()

# Delete an Order Item by ID
@app.route('/order-items/<int:order_item_id>', methods=['DELETE'])
def delete_order_item():
    return view.delete_order_item()