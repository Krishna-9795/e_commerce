from e_commerce.app import app
from e_commerce.payments import view
from flask import Blueprint

payment_bp=Blueprint('payments',__name__)

# Create a Payment
@payment_bp.route('/payments/register', methods=['POST'])
def create_payment():
    return view.create_payment()

# Retrieve a Payment by ID
@payment_bp.route('/payments/retrieve/<int:payment_id>', methods=['GET'])
def get_payment():
    return view.get_payment()
# Update a Payment by ID
@payment_bp.route('/payments/update/<int:payment_id>', methods=['PUT'])
def update_payment():
    view.update_payment()
# Delete a Payment by ID
@payment_bp.route('/payments/delete/<int:payment_id>', methods=['DELETE'])
def delete_payment():
    return view.delete_payment()

# Create a Payment Method
@payment_bp.route('/payments/payment-methods/register', methods=['POST'])
def create_payments_method():
    return view.create_payment_method()

# Retrieve a Payment Method by ID
@payment_bp.route('/payments/payment-methods/retrieve/<int:payment_method_id>', methods=['GET'])
def get_payment_method():
    return view.get_payment_method()

# Update a Payment Method by ID
@payment_bp.route('/payments/payment-methods/update/<int:payment_method_id>', methods=['PUT'])
def update_payment_method():
    return view.update_payment_method()
# Delete a Payment Method by ID
@payment_bp.route('/payments/payment-methods/delete/<int:payment_method_id>', methods=['DELETE'])
def delete_payment_method():
    return view.delete_payment_method()
# Create a Transaction
@payment_bp.route('/payments/transactions', methods=['POST'])
def create_transaction():
    return view.create_transaction()

# Retrieve a Transaction by ID
@payment_bp.route('/payments/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction():
    return view.get_transaction()

# Update a Transaction by ID
@payment_bp.route('/payments/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction():
    return view.update_transaction()

# Delete a Transaction by ID
@payment_bp.route('/payments/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction():
    return view.delete_transaction()