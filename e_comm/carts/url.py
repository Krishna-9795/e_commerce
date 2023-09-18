from e_comm.app import app
from e_comm.carts import view


def cart_routes(app):
    # Create a Cart
    @app.route('/carts', methods=['POST'])
    def create_carts():
        return view.create_cart()

    # Retrieve a Cart by ID
    @app.route('/carts/retrieve/<int:cart_id>', methods=['GET'])
    def get_carts():
        return view.get_cart()

    # Update a Cart by ID
    @app.route('/carts/<int:cart_id>', methods=['PUT'])
    def update_carts():
        return view.update_cart()

    # Delete a Cart by ID
    @app.route('/carts/update/<int:cart_id>', methods=['DELETE'])
    def delete_carts():
        return view.delete_cart()

    # Create a Cart Item
    @app.route('/cart_items', methods=['POST'])
    def create_cart_items():
        return view.create_cart_item()

    # Retrieve a Cart Item by ID
    @app.route('/cart_items/retrieve/<int:cart_item_id>', methods=['GET'])
    def get_cart_items():
        return view.get_cart_item()

    # Update a Cart Item by ID
    @app.route('/cart_items/update/<int:cart_item_id>', methods=['PUT'])
    def update_cart_items():
        return view.update_cart_item()

    # Delete a Cart Item by ID
    @app.route('/cart_items/delete/<int:cart_item_id>', methods=['DELETE'])
    def delete_cart_item():
        return view.delete_cart_item()