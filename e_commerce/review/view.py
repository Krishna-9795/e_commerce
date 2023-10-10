from flask import jsonify,request
from e_commerce.db import db
from e_commerce.review.models import Reviews
from datetime import datetime

#Create a Review
def create_review():
    try:
        data = request.json
        new_review = Reviews(
            user_id=data['user_id'],
            product_id=data['product_id'],
            rating=data['rating'],
            review_text=data['review_text'],
            review_date=data.get('review_date',datetime.utcnow())
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'message': 'Review created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Retrieve all Reviews
def get_reviews():
    reviews = Reviews.query.all()
    review_list = [{"review_id":review.review_id,
                        "user_id":review.user_id,
                        "product_id":review.product_id,
                        "rating":review.rating,
                        "review_text":review.review_text,
                        "review_date":review.review_date} for review in reviews]
    return jsonify(review_list), 200

# Retrieve a Review by ID
def get_review(review_id):
    review = Reviews.query.get(review_id)
    if review:
        return jsonify({"review_id":review.review_id,
                        "user_id":review.user_id,
                        "product_id":review.product_id,
                        "rating":review.rating,
                        "review_text":review.review_text,
                        "review_date":review.review_date}), 200
    else:
        return jsonify({'message': 'Review not found'}), 404
    
# Update a Review by ID
def update_review(review_id):
    review = Reviews.query.get(review_id)
    if not review:
        return jsonify({'message': 'Review not found'}), 404

    data = request.json
    review.user_id = data.get('user_id', review.user_id)
    review.product_id = data.get('product_id', review.product_id)
    review.rating = data.get('rating', review.rating)
    review.review_text = data.get('review_text', review.review_text)
    review.review_date = data.get('review_date', review.review_date)

    db.session.commit()
    return jsonify({'message': 'Review updated successfully'}), 200

# Delete a Review by ID
def delete_review(review_id):
    review = Reviews.query.get(review_id)
    if not review:
        return jsonify({'message': 'Review not found'}), 404

    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'}), 200



