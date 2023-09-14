from e_comm.app import app
from e_comm.coupons import view


# Create a Coupon
@app.route('/coupons', methods=['POST'])
def create_coupon():
    return view.create_coupon()

# Retrieve all Coupons
@app.route('/coupons', methods=['GET'])
def get_coupons():
    return view.get_coupons()


# Retrieve a Coupon by ID
@app.route('/coupons/<int:coupon_id>', methods=['GET'])
def get_coupon():
    return view.get_coupon()

# Update a Coupon by ID
@app.route('/coupons/<int:coupon_id>', methods=['PUT'])
def update_coupon():
    return view.update_coupon()

# Delete a Coupon by ID
@app.route('/coupons/<int:coupon_id>', methods=['DELETE'])
def delete_coupon():
    return view.delete_coupon()
