from flask_jwt_extended import jwt_required
from e_commerce.user.view import register, login, get_user, get_all_users,update_user, delete_user
from e_commerce.product.view import get_product,get_all_products,get_product_variant
from e_commerce.addresses.view import address_data,update_address,get_address,delete_address,shipping_address_data,get_ship_address,update_shipping_address,delete_shipping_address
from e_commerce.carts.view import create_cart,get_cart,update_cart,delete_cart,create_cart_item,get_cart_item,update_cart_item,delete_cart_item
from e_commerce.orders.view import create_order,get_order,create_order_item,get_order_item,update_order_item,delete_order_item
from e_commerce.coupons.view import get_coupons,get_coupon
from e_commerce.payments.view import create_payment,get_payment,get_payment_method,create_transaction,get_transaction
from e_commerce.review.view import get_review,get_review,update_review,delete_review

from flask import Blueprint

user_bp = Blueprint('user', __name__)

# Registering
@user_bp.route('/user/register', methods=['POST'])
def registers():
        return register()
# login
@user_bp.route('/user/login', methods=['POST'])
def login_routes():
    return login()

# Getting the user details according to user_id
@user_bp.route('/user/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_route(user_id):
    return get_user(user_id)

# Getting the list of users
@user_bp.route('/user/user_retrieval', methods=['GET'])
@jwt_required()
def get_all_users_route():
    return get_all_users()


# Update
@user_bp.route('user/update/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_route(user_id):
    return update_user(user_id)
# Delete
@user_bp.route('user/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_route(user_id):
    return delete_user(user_id)



@user_bp.route('/address/register',methods=['POST'])
@jwt_required()
def addresses_data():
    return address_data()
    
@user_bp.route('/user/address/update/<int:address_id>',methods=['PUT']) 
@jwt_required()
def update_addresses(address_id):
    return update_address(address_id)

# Retrieve address
@user_bp.route('/user/address/get/<int:address_id>',methods=['get'])
def gets_address(address_id):
    return get_address(address_id) 

# Delete
@user_bp.route('/user/address/delete/<int:address_id>', methods=['DELETE'])
# @jwt_required()
def delete_addresses(address_id):
    return delete_address(address_id)

# Creating a shipping address
@user_bp.route('/user/address/shipping_addresses',methods=['POST'])
#  @jwt_required()
def ship_addresses_data():
    return shipping_address_data()

# Retrieving a shipping address
@user_bp.route('/user/shipping_address/get/<int:address_id>',methods=['get'])
def gets_ship_address(address_id):
    return get_ship_address(address_id) 


# Updating a shipping address
@user_bp.route('/user/address/shipping_address/update/<int:address_id>',methods=['PUT']) 
#   @jwt_required()
def update_ship_addresses(address_id):
    return update_shipping_address(address_id)

# Deleting a shipping address
@user_bp.route('/user/address/shipping_address/delete/<int:address_id>', methods=['DELETE'])
#  @jwt_required()
def delete_shipping_addresses(address_id):
    return delete_shipping_address(address_id)

# Create a Cart
@user_bp.route('/user/carts/create', methods=['POST'])
def create_carts():
    return create_cart()

# Retrieve a Cart by ID
@user_bp.route('/user/carts/retrieve/<int:cart_id>', methods=['GET'])
def get_carts(cart_id):
    return get_cart(cart_id)

# Update a Cart by ID
@user_bp.route('/user/carts/update/<int:cart_id>', methods=['PUT'])
def update_carts(cart_id):
    return update_cart(cart_id)

# Delete a Cart by ID
@user_bp.route('/user/carts/delete/<int:cart_id>', methods=['DELETE'])
def delete_carts(cart_id):
    return delete_cart(cart_id)

# Create a Cart Item
@user_bp.route('/user/carts/cart_items/create', methods=['POST'])
def create_cart_items():
    return create_cart_item()

# Retrieve a Cart Item by ID
@user_bp.route('/user/carts/cart_items/retrieve/<int:cart_item_id>', methods=['GET'])
def get_cart_items(cart_item_id):
    return  get_cart_item(cart_item_id)

# Update a Cart Item by ID
@user_bp.route('/user/carts/cart_items/update/<int:cart_item_id>', methods=['PUT'])
def update_cart_items(cart_item_id):
    return update_cart_item(cart_item_id)

# Delete a Cart Item by ID
@user_bp.route('/user/carts/cart_items/delete/<int:cart_item_id>', methods=['DELETE'])
def delete_cart_item(cart_item_id):
    return delete_cart_item(cart_item_id)

from e_commerce.coupons import view
# Retrieve all Coupons
@user_bp.route('user/coupons/retrieve', methods=['GET'])
def get_coupons():
    return  get_coupons()


# Retrieve a Coupon by ID
@user_bp.route('user/coupons/retrieve/<int:coupon_id>', methods=['GET'])
def get_coupon(coupon_id):
    return get_coupon(coupon_id)



# Retrieve all Reviews
@user_bp.route('/user/reviews/retrieve', methods=['GET'])
def get_reviews():
    return get_review()

# Retrieve a Review by ID
@user_bp.route('/user/reviews/retrieve/<int:review_id>', methods=['GET'])
def get_review(review_id):
    return get_review(review_id)

# Update a Review by ID
@user_bp.route('/user/reviews/update/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    return update_review(review_id)

# Delete a Review by ID
@user_bp.route('/user/reviews/delete/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    return delete_review(review_id)

from e_commerce.product import view
# Retrieve a Product
@user_bp.route('/user/products/retrieve/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return get_product(product_id)
# Gets all the products
@user_bp.route('/user/products/retrieve', methods=['GET'])
def get_products():
    return get_all_products()

# Retrieve all Product Variant
@user_bp.route('/user/products/product-variants/retrieve>', methods=['GET'])
def get_all_product_variants():
    return get_all_product_variants()

# Retrieve a Product Variant
@user_bp.route('/user/user/products/product-variants/retrieve/<int:variant_id>', methods=['GET'])
def get_product_variants(variant_id):
    return get_product_variant(variant_id)

from e_commerce.payments import view
# Create a Payment
@user_bp.route('/user/payments/create', methods=['POST'])
def create_payment():
    return create_payment()
# Retrieve a Payment by ID
@user_bp.route('/user/payments/retrieve/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    return get_payment(payment_id)
# Retrieve a Payment Method by ID
@user_bp.route('/user/payments/payment_methods/retrieve/<int:payment_method_id>', methods=['GET'])
def get_payment_method(payment_method_id):
    return get_payment_method(payment_method_id)
@user_bp.route('/user/payments/transactions', methods=['POST'])
def create_transaction():
    return create_transaction()

# Retrieve a Transaction by ID
@user_bp.route('/user/payments/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    return get_transaction(transaction_id)


# Create an Order 
@user_bp.route('/user/orders/register', methods=['POST'])
def create_orders():
    return create_order()

#Return an order by id
@user_bp.route('/user/orders/retrieve/<int:order_id>', methods=['GET'])
def get_orders(order_id):
    return get_order(order_id)

# Create an Order Item
@user_bp.route('/user/order-items/register', methods=['POST'])
def create_order_items():
    return create_order_item()

# Retrieve an Order Item by ID
@user_bp.route('/user/order-items/retrieve/<int:order_item_id>', methods=['GET'])
def get_order_item(order_item_id):
    return get_order_item(order_item_id)

# Update an Order Item by ID
@user_bp.route('/user/order-items/update/<int:order_item_id>', methods=['PUT'])
def update_order_item(order_item_id):
    return update_order_item(order_item_id)

# Delete an Order Item by ID
@user_bp.route('/user/order-items/delete/<int:order_item_id>', methods=['DELETE'])
def delete_order_item(order_item_id):
    return delete_order_item(order_item_id)