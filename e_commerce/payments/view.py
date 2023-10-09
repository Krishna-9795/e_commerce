from e_commerce.db import db
from flask import request,jsonify
from e_commerce.payments.models import Payments,PaymentMethods,Transactions


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
        return jsonify({"payment_id":payment.payment_id,
                        "order_id":payment.order_id,
                        "payment_date":payment.payment_date,
                        "payment_amount":payment.payment_amount,
                        "payment_status":payment.payment_status,
                        "payment_method":payment.payment_method
                        }), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404
# Update a Payment by ID
def update_payment(payment_id):
    try:
        data = request.json
        payment = Payments.query.get(payment_id)
        if not payment:
            return jsonify({'message': 'Payment not found'}), 404

        
        payment.order_id = data.get('order_id', payment.order_id)
        payment.payment_date = data.get('payment_date', payment.payment_date)
        payment.payment_amount = data.get('payment_amount', payment.payment_amount)
        payment.payment_status = data.get('payment_status', payment.payment_status)
        payment.payment_method = data.get('payment_method', payment.payment_method)

        db.session.commit()
        return jsonify({'message': 'Payment updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        return jsonify({"payment_method_id":payment_method.payment_method_id,
                        "user_id":payment_method.user_id,
                        "card_number":payment_method.card_number,
                        "expiration_date":payment_method.expiration_date,
                        "cvv":payment_method.cvv }), 200
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

# Create a Transaction
def create_transaction():
    try:
        data = request.json
        new_transaction = Transactions(
            user_id=data['user_id'],
            transaction_amount=data['transaction_amount'],
            transaction_type=data['transaction_type']
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve a Transaction by ID
def get_transaction(transaction_id):
    transaction = Transactions.query.get(transaction_id)
    if transaction:
        return jsonify({"transaction_id":transaction.transaction_id,
                        "user_id":transaction.user_id,
                        "transaction_amount":transaction.transaction_amount,
                        "transaction_type":transaction.transaction_type}), 200
    else:
        return jsonify({'message': 'Transaction not found'}), 404

# Update a Transaction by ID
def update_transaction(transaction_id):
    transaction = Transactions.query.get(transaction_id)
    if not transaction:
        return jsonify({'message': 'Transaction not found'}), 404

    data = request.json
    transaction.user_id = data.get('user_id', transaction.user_id)
    transaction.transaction_amount = data.get('transaction_amount', transaction.transaction_amount)
    transaction.transaction_type = data.get('transaction_type', transaction.transaction_type)

    db.session.commit()
    return jsonify({'message': 'Transaction updated successfully'}), 200

# Delete a Transaction by ID
def delete_transaction(transaction_id):
    transaction = Transactions.query.get(transaction_id)
    if not transaction:
        return jsonify({'message': 'Transaction not found'}), 404

    db.session.delete(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction deleted successfully'}), 200







