from e_comm.app import db
from e_comm.orders.models import Orders,OrderItems
from flask import request,jsonify

def create_order():
    try:
        data = request.json
        new_order = Orders(
            user_id=data['user_id'],
            order_date=data['order_date'],
            total_amount=data['total_amount'],
            order_status=data.get('order_status'),
            shipping_address=data.get('shipping_address'),
            payment_method=data.get('payment_method'),
            coupon_id=data.get('coupon_id')
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Retun an order by id  
def get_order(order_id):
    order = Orders.query.get(order_id)
    if order:
        return jsonify(order.serialize()), 200
    else:
        return jsonify({'message': 'Order not found'}), 404
    
# Update an Order
def update_order(order_id):
    order = Orders.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    data = request.json
    order.user_id = data.get('user_id', order.user_id)
    order.order_date = data.get('order_date', order.order_date)
    order.total_amount = data.get('total_amount', order.total_amount)
    order.order_status = data.get('order_status', order.order_status)
    order.shipping_address = data.get('shipping_address', order.shipping_address)
    order.payment_method = data.get('payment_method', order.payment_method)
    order.coupon_id = data.get('coupon_id', order.coupon_id)

    db.session.commit()
    return jsonify({'message': 'Order updated successfully'}), 200

def delete_order(order_id):
    order = Orders.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

# Creating an Order Item 
def create_order_item():
    try:
        data = request.json
        new_order_item = OrderItems(
            order_id=data['order_id'],
            product_id=data['product_id'],
            unit_price=data['unit_price'],
            order_quantity=data['order_quantity'],
            discount_percentage=data.get('discount_percentage'),
            total_amount=data['total_amount']
        )
        db.session.add(new_order_item)
        db.session.commit()
        return jsonify({'message': 'Order item created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Retreiving an Order Item   
def get_order_item(order_item_id):
    order_item = OrderItems.query.get(order_item_id)
    if order_item:
        return jsonify(order_item.serialize()), 200
    else:
        return jsonify({'message': 'Order item not found'}), 404
    
# Update an Order Item by ID
def update_order_item(order_item_id):
    order_item = OrderItems.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404

    data = request.json
    order_item.order_id = data.get('order_id', order_item.order_id)
    order_item.product_id = data.get('product_id', order_item.product_id)
    order_item.unit_price = data.get('unit_price', order_item.unit_price)
    order_item.order_quantity = data.get('order_quantity', order_item.order_quantity)
    order_item.discount_percentage = data.get('discount_percentage', order_item.discount_percentage)
    order_item.total_amount = data.get('total_amount', order_item.total_amount)

    db.session.commit()
    return jsonify({'message': 'Order item updated successfully'}), 200

# Delete an Order Item by ID
def delete_order_item(order_item_id):
    order_item = OrderItems.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404

    db.session.delete(order_item)
    db.session.commit()
    return jsonify({'message': 'Order item deleted successfully'}), 200




