from e_commerce.db import db
from e_commerce.carts.models import Carts,Cart_items
from flask import jsonify,request
import datetime

# Create a Cart
def create_cart():
    try:
        data = request.json
        new_cart = Carts(
            user_id=data['user_id'],
            creation_date=data.get('creation_date', datetime.utcnow())
        )
        db.session.add(new_cart)
        db.session.commit()
        return jsonify({'message': 'Cart created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve a Cart by ID
def get_cart(cart_id):
    cart = Carts.query.get(cart_id)
    if cart:
        return jsonify(cart.serialize()), 200
    else:
        return jsonify({'message': 'Cart not found'}), 404
# Update a Cart by ID
def update_cart(cart_id):
    cart = Carts.query.get(cart_id)
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    data = request.json
    cart.user_id = data.get('user_id', cart.user_id)
    cart.creation_date = data.get('creation_date', cart.creation_date)

    db.session.commit()
    return jsonify({'message': 'Cart updated successfully'}), 200

# Delete a Cart by ID
def delete_cart(cart_id):
    cart = Carts.query.get(cart_id)
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    db.session.delete(cart)
    db.session.commit()
    return jsonify({'message': 'Cart deleted successfully'}), 200

# Create a Cart Item
def create_cart_item():
    try:
        data = request.json
        new_cart_item = Cart_items(
            cart_id=data['cart_id'],
            product_id=data['product_id'],
            quantity=data['quantity']
        )
        db.session.add(new_cart_item)
        db.session.commit()
        return jsonify({'message': 'Cart item created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Retrieve cart item by id
def get_cart_item(cart_item_id):
    cart_item = Cart_items.query.get(cart_item_id)
    if cart_item:
        return jsonify(cart_item.serialize()), 200
    else:
        return jsonify({'message': 'Cart item not found'}), 404

# Update a Cart Item by ID
def update_cart_item(cart_item_id):
    cart_item = Cart_items.query.get(cart_item_id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found'}), 404

    data = request.json
    cart_item.cart_id = data.get('cart_id', cart_item.cart_id)
    cart_item.product_id = data.get('product_id', cart_item.product_id)
    cart_item.quantity = data.get('quantity', cart_item.quantity)

    db.session.commit()
    return jsonify({'message': 'Cart item updated successfully'}), 200
# Deletes a Cart Item by ID
def delete_cart_item(cart_item_id):
    cart_item = Cart_items.query.get(cart_item_id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found'}), 404

    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Cart item deleted successfully'}), 200
