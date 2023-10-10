from flask import jsonify,request
from e_commerce.db import db
from e_commerce.coupons.models import Coupons


# Create a Coupon
def create_coupon():
    try:
        data = request.json
        new_coupon = Coupons(
            code=data['code'],
            coupon_amount=data['coupon_amount'],
            coupon_expiration_date=data.get('coupon_expiration_date')
        )
        db.session.add(new_coupon)
        db.session.commit()
        return jsonify({'message': 'Coupon created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve all Coupons
def get_coupons():
    coupons = Coupons.query.all()
    coupon_list = [{"coupon_id":coupons.coupon_id,
                    "code":coupons.code,
                    "coupon_amount":coupons.coupon_amount,
                    "coupon_expiration_date":coupons.coupon_expiration_date} for coupons in coupons]
    return jsonify(coupon_list), 200

# Retrieve a Coupon by ID
def get_coupon(coupon_id):
    coupons = Coupons.query.get(coupon_id)
    if coupons:
        return jsonify({"coupon_id":coupons.coupon_id,
                    "code":coupons.code,
                    "coupon_amount":coupons.coupon_amount,
                    "coupon_expiration_date":coupons.coupon_expiration_date}), 200
    else:
        return jsonify({'message': 'Coupon not found'}), 404

# Update a Coupon by ID
def update_coupon(coupon_id):
    coupon = Coupons.query.get(coupon_id)
    if not coupon:
        return jsonify({'message': 'Coupon not found'}), 404

    data = request.json
    coupon.code = data.get('code', coupon.code)
    coupon.coupon_amount = data.get('coupon_amount', coupon.coupon_amount)
    coupon.coupon_expiration_date = data.get('coupon_expiration_date', coupon.coupon_expiration_date)

    db.session.commit()
    return jsonify({'message': 'Coupon updated successfully'}), 200

# Delete a Coupon by ID
def delete_coupon(coupon_id):
    coupon = Coupons.query.get(coupon_id)
    if not coupon:
        return jsonify({'message': 'Coupon not found'}), 404

    db.session.delete(coupon)
    db.session.commit()
    return jsonify({'message': 'Coupon deleted successfully'}), 200