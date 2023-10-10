from flask_jwt_extended import jwt_required
from e_commerce.user import view
from e_commerce.addresses import view
from e_commerce.carts import view

from e_commerce.orders import view
from e_commerce.payments import view
from e_commerce.product import view
from e_commerce.review import view
from flask import Blueprint

user_bp = Blueprint('user', __name__)

# Registering
@user_bp.route('/user/register', methods=['POST'])
def registers():
        return view.register()
# login
@user_bp.route('/user/login', methods=['POST'])
def login_routes():
    return view.login()

# Getting the user details according to user_id
@user_bp.route('/user/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_route(user_id):
    return view.get_user(user_id)

# Getting the list of users
@user_bp.route('/user/user_retrieval', methods=['GET'])
@jwt_required()
def get_all_users_route():
    return view.get_all_users()


# Update
@user_bp.route('user/update/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_route(user_id):
    return view.update_user(user_id)
# Delete
@user_bp.route('user/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_route(user_id):
    return view.delete_user(user_id)



@user_bp.route('/address/register',methods=['POST'])
#@jwt_required()
def addresses_data():
    return view.address_data()
    
@user_bp.route('/user/address/update/<int:address_id>',methods=['PUT']) 
# @jwt_required()
def update_addresses(address_id):
    return view.update_address(address_id)

# Retrieve address
@user_bp.route('/user/address/get/<int:address_id>',methods=['get'])
def gets_address(address_id):
    return view.get_address(address_id) 

# Delete
@user_bp.route('/user/address/delete/<int:address_id>', methods=['DELETE'])
# @jwt_required()
def delete_addresses(address_id):
    return view.delete_address(address_id)

# Creating a shippping address
@user_bp.route('/user/address/shipping_addresses',methods=['POST'])
#  @jwt_required()
def ship_addresses_data():
    return view.shipping_address_data()

# Retrieving a shipping address
@user_bp.route('/user/shipping_address/get/<int:address_id>',methods=['get'])
def gets_ship_address(address_id):
    return view.get_ship_address(address_id) 


# Updating a shipping address
@user_bp.route('/user/address/shipping_address/update/<int:address_id>',methods=['PUT']) 
#   @jwt_required()
def update_ship_addresses(address_id):
    return view.update_shipping_address(address_id)

# Deleting a shipping address
@user_bp.route('/user/address/shipping_address/delete/<int:address_id>', methods=['DELETE'])
#  @jwt_required()
def delete_shipping_addresses(address_id):
    return view.delete_shipping_address(address_id)

# Create a Cart
@user_bp.route('/user/carts/create', methods=['POST'])
def create_carts():
    return view.create_cart()

# Retrieve a Cart by ID
@user_bp.route('/user/carts/retrieve/<int:cart_id>', methods=['GET'])
def get_carts(cart_id):
    return view.get_cart(cart_id)

# Update a Cart by ID
@user_bp.route('/user/carts/update/<int:cart_id>', methods=['PUT'])
def update_carts(cart_id):
    return view.update_cart(cart_id)

# Delete a Cart by ID
@user_bp.route('/user/carts/delete/<int:cart_id>', methods=['DELETE'])
def delete_carts(cart_id):
    return view.delete_cart(cart_id)

# Create a Cart Item
@user_bp.route('/user/carts/cart_items/create', methods=['POST'])
def create_cart_items():
    return view.create_cart_item()

# Retrieve a Cart Item by ID
@user_bp.route('/user/carts/cart_items/retrieve/<int:cart_item_id>', methods=['GET'])
def get_cart_items(cart_item_id):
    return view.get_cart_item(cart_item_id)

# Update a Cart Item by ID
@user_bp.route('/user/carts/cart_items/update/<int:cart_item_id>', methods=['PUT'])
def update_cart_items(cart_item_id):
    return view.update_cart_item(cart_item_id)

# Delete a Cart Item by ID
@user_bp.route('/user/carts/cart_items/delete/<int:cart_item_id>', methods=['DELETE'])
def delete_cart_item(cart_item_id):
    return view.delete_cart_item(cart_item_id)

from e_commerce.coupons import view
# Retrieve all Coupons
@user_bp.route('user/coupons/retrieve', methods=['GET'])
def get_coupons():
    return view.get_coupons()


# Retrieve a Coupon by ID
@user_bp.route('user/coupons/retrieve/<int:coupon_id>', methods=['GET'])
def get_coupon(coupon_id):
    return view.get_coupon(coupon_id)



# Retrieve all Reviews
@user_bp.route('/user/reviews/retrieve', methods=['GET'])
def get_reviews():
    return view.get_review()

# Retrieve a Review by ID
@user_bp.route('/user/reviews/retrieve/<int:review_id>', methods=['GET'])
def get_review(review_id):
    return view.get_review(review_id)

# Update a Review by ID
@user_bp.route('/user/reviews/update/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    return view.update_review(review_id)

# Delete a Review by ID
@user_bp.route('/user/reviews/delete/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    return view.delete_review(review_id)

from e_commerce.product import view
# Retrieve a Product
@user_bp.route('/user/products/retrieve/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return view.get_product(product_id)
# Gets all the products
@user_bp.route('/user/products/retrieve', methods=['GET'])
def get_products():
    return view.get_all_products()

# Retrieve all Product Variant
@user_bp.route('/user/products/product-variants/retrieve>', methods=['GET'])
def get_all_product_variants():
    return view.get_all_product_variants()

# Retrieve a Product Variant
@user_bp.route('/user/user/products/product-variants/retrieve/<int:variant_id>', methods=['GET'])
def get_product_variants(variant_id):
    return view.get_product_variant(variant_id)

from e_commerce.payments import view
# Create a Payment
@user_bp.route('/user/payments/create', methods=['POST'])
def create_payment():
    return view.create_payment()
# Retrieve a Payment by ID
@user_bp.route('/user/payments/retrieve/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    return view.get_payment(payment_id)
# Retrieve a Payment Method by ID
@user_bp.route('/user/payments/payment_methods/retrieve/<int:payment_method_id>', methods=['GET'])
def get_payment_method(payment_method_id):
    return view.get_payment_method(payment_method_id)
@user_bp.route('/user/payments/transactions', methods=['POST'])
def create_transaction():
    return view.create_transaction()

# Retrieve a Transaction by ID
@user_bp.route('/user/payments/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    return view.get_transaction(transaction_id)


# Create an Order 
@user_bp.route('/user/orders/register', methods=['POST'])
def create_orders():
    return view.create_order()

#Return an order by id
@user_bp.route('/user/orders/retrieve/<int:order_id>', methods=['GET'])
def get_orders(order_id):
    return view.get_order(order_id)




# Create an Order Item
@user_bp.route('/user/order-items/register', methods=['POST'])
def create_order_items():
    return view.create_order_item()

# Retrieve an Order Item by ID
@user_bp.route('/user/order-items/retrieve/<int:order_item_id>', methods=['GET'])
def get_order_item(order_item_id):
    return view.get_order_item(order_item_id)

# Update an Order Item by ID
@user_bp.route('/user/order-items/update/<int:order_item_id>', methods=['PUT'])
def update_order_item(order_item_id):
    return view.update_order_item(order_item_id)

# Delete an Order Item by ID
@user_bp.route('/user/order-items/delete/<int:order_item_id>', methods=['DELETE'])
def delete_order_item(order_item_id):
    return view.delete_order_item(order_item_id)