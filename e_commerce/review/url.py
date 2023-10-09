from e_commerce.review import view
from flask import Blueprint

review_bp = Blueprint('reviews', __name__)

# Create a Review
@review_bp.route('/reviews/register', methods=['POST'])
def create_review():
    return view.create_review()

# Retrieve all Reviews
@review_bp.route('/reviews/retrieve', methods=['GET'])
def get_reviews():
    return view.get_review()

# Retrieve a Review by ID
@review_bp.route('/reviews/retrieve/<int:review_id>', methods=['GET'])
def get_review(review_id):
    return view.get_review(review_id)

# Update a Review by ID
@review_bp.route('/reviews/update/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    return view.update_review(review_id)

# Delete a Review by ID
@review_bp.route('/reviews/delete/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    return view.delete_review(review_id)