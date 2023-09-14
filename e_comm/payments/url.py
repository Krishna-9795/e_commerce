from e_comm.app import app
from e_comm.payments import view

# Create a Payment
@app.route('/payments', methods=['POST'])
def create_payment():
    return view.create_payment()

# Retrieve a Payment by ID
@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment():
    return view.get_payment()
# Update a Payment by ID
@app.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment():
    view.update_payment()
# Delete a Payment by ID
@app.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment():
    return view.delete_payment()

# Create a Payment Method
@app.route('/payment-methods', methods=['POST'])
def create_payments_method():
    return view.create_payment_method()

# Retrieve a Payment Method by ID
@app.route('/payment-methods/<int:payment_method_id>', methods=['GET'])
def get_payment_method():
    return view.get_payment_method()

# Update a Payment Method by ID
@app.route('/payment-methods/<int:payment_method_id>', methods=['PUT'])
def update_payment_method():
    return view.update_payment_method()
# Delete a Payment Method by ID
@app.route('/payment-methods/<int:payment_method_id>', methods=['DELETE'])
def delete_payment_method():
    return view.delete_payment_method()