from e_commerce.payments import view
from flask import Blueprint

payment_bp=Blueprint('payments',__name__)


# Create a Payment
@payment_bp.route('/payments/create', methods=['POST'])
def create_payment():
    return view.create_payment()

# Retrieve a Payment by ID
@payment_bp.route('/payments/retrieve/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    return view.get_payment(payment_id)
# Update a Payment by ID
@payment_bp.route('/payments/update/<int:payment_id>', methods=['PUT'])
def update_payments(payment_id):
    view.update_payment(payment_id) 
# Delete a Payment by ID
@payment_bp.route('/payments/delete/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    return view.delete_payment(payment_id)

# Create a Payment Method
@payment_bp.route('/payments/payment_methods/create', methods=['POST'])
def create_payments_method():
    return view.create_payment_method()

# Retrieve a Payment Method by ID
@payment_bp.route('/payments/payment_methods/retrieve/<int:payment_method_id>', methods=['GET'])
def get_payment_method(payment_method_id):
    return view.get_payment_method(payment_method_id)

# Update a Payment Method by ID
@payment_bp.route('/payments/payment_methods/update/<int:payment_method_id>', methods=['PUT'])
def update_payment_method(payment_method_id):
    return view.update_payment_method(payment_method_id)
# Delete a Payment Method by ID
@payment_bp.route('/payments/payment_methods/delete/<int:payment_method_id>', methods=['DELETE'])
def delete_payment_method(payment_method_id):
    return view.delete_payment_method(payment_method_id)
# Create a Transaction
@payment_bp.route('/payments/transactions', methods=['POST'])
def create_transaction():
    return view.create_transaction()

# Retrieve a Transaction by ID
@payment_bp.route('/payments/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    return view.get_transaction(transaction_id)

# Update a Transaction by ID
@payment_bp.route('/payments/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    return view.update_transaction(transaction_id)

# Delete a Transaction by ID
@payment_bp.route('/payments/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    return view.delete_transaction(transaction_id)