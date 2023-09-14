from e_comm.app import db
from flask import request,jsonify
from e_comm.payments import Payments,PaymentMethods,Transactions


# Create a Payment
def create_payment():
    try:
        data = request.json
        new_payment = Payments(
            order_id=data['order_id'],
            payment_date=data['payment_date'],
            payment_amount=data['payment_amount'],
            payment_status=data['payment_status'],
            payment_method=data.get('payment_method')
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({'message': 'Payment created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Retrieve a Payment by ID
def get_payment(payment_id):
    payment = Payments.query.get(payment_id)
    if payment:
        return jsonify(payment.serialize()), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404
# Update a Payment by ID
def update_payment(payment_id):
    payment = Payments.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404

    data = request.json
    payment.order_id = data.get('order_id', payment.order_id)
    payment.payment_date = data.get('payment_date', payment.payment_date)
    payment.payment_amount = data.get('payment_amount', payment.payment_amount)
    payment.payment_status = data.get('payment_status', payment.payment_status)
    payment.payment_method = data.get('payment_method', payment.payment_method)

    db.session.commit()
    return jsonify({'message': 'Payment updated successfully'}), 200

# Delete a Payment by ID
def delete_payment(payment_id):
    payment = Payments.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404

    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted successfully'}), 200
# # Create a Payment Method
def create_payment_method():
    try:
        data = request.json
        new_payment_method = PaymentMethods(
            user_id=data['user_id'],
            card_number=data['card_number'],
            expiration_date=data['expiration_date'],
            cvv=data['cvv']
        )
        db.session.add(new_payment_method)
        db.session.commit()
        return jsonify({'message': 'Payment method created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Retrieve a Payment Method by ID
def get_payment_method(payment_method_id):
    payment_method = PaymentMethods.query.get(payment_method_id)
    if payment_method:
        return jsonify(payment_method.serialize()), 200
    else:
        return jsonify({'message': 'Payment method not found'}), 404
# Update a Payment Method by ID
def update_payment_method(payment_method_id):
    payment_method = PaymentMethods.query.get(payment_method_id)
    if not payment_method:
        return jsonify({'message': 'Payment method not found'}), 404

    data = request.json
    payment_method.user_id = data.get('user_id', payment_method.user_id)
    payment_method.card_number = data.get('card_number', payment_method.card_number)
    payment_method.expiration_date = data.get('expiration_date', payment_method.expiration_date)
    payment_method.cvv = data.get('cvv', payment_method.cvv)

    db.session.commit()
    return jsonify({'message': 'Payment method updated successfully'}), 200

# Delete a Payment Method by ID
def delete_payment_method(payment_method_id):
    payment_method = PaymentMethods.query.get(payment_method_id)
    if not payment_method:
        return jsonify({'message': 'Payment method not found'}), 404

    db.session.delete(payment_method)
    db.session.commit()
    return jsonify({'message': 'Payment method deleted successfully'}), 200
