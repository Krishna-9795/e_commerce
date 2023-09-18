from e_comm.app import app
from e_comm.review import view

def review_routes(app):
    # Create a Review
    @app.route('/reviews', methods=['POST'])
    def create_review():
        return view.create_review()

    # Retrieve all Reviews
    @app.route('/reviews', methods=['GET'])
    def get_reviews():
        return view.get_review()

    # Retrieve a Review by ID
    @app.route('/reviews/<int:review_id>', methods=['GET'])
    def get_review():
        return view.get_review()

    # Update a Review by ID
    @app.route('/reviews/<int:review_id>', methods=['PUT'])
    def update_review():
        return view.update_review()

    # Delete a Review by ID
    @app.route('/reviews/<int:review_id>', methods=['DELETE'])
    def delete_review():
        return view.delete_review()