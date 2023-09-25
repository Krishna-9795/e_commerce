from e_commerce.coupons import view
from flask import Blueprint

coupon_bp = Blueprint('coupons', __name__)
    

# Create a Coupon
@coupon_bp.route('/coupons/register', methods=['POST'])
def create_coupon():
    return view.create_coupon()

# Retrieve all Coupons
@coupon_bp.route('/coupons/retrieve', methods=['GET'])
def get_coupons():
    return view.get_coupons()


# Retrieve a Coupon by ID
@coupon_bp.route('/coupons/retrieve/<int:coupon_id>', methods=['GET'])
def get_coupon():
    return view.get_coupon()

# Update a Coupon by ID
@coupon_bp.route('/coupons/update/<int:coupon_id>', methods=['PUT'])
def update_coupon():
    return view.update_coupon()

# Delete a Coupon by ID
@coupon_bp.route('/coupons/delete/<int:coupon_id>', methods=['DELETE'])
def delete_coupon():
    return view.delete_coupon()
