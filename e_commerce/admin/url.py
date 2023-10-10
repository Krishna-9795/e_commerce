
#from e_commerce.utils import admin_token
from e_commerce.admin import view
from e_commerce.product import view
from e_commerce.addresses import view
from e_commerce.user import view
from e_commerce.carts import view
from e_commerce.review import view
from e_commerce.payments import view
from e_commerce.orders import view
from e_commerce.coupons import view
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/register',methods=['POST'])
def admin_reg():
    return view.admin_register()

@admin_bp.route('/admin/login/' , methods = ['POST'])
def admin_login():
    return view.admin_login()

@admin_bp.route('/admin/get/' , methods = ['GET'])
def admin_login():
    return view.admin_login()


@admin_bp.route('/admin/product/create',methods=['POST'])
def admin_prod_create():
    return view.create_product()

@admin_bp.route('admin/products/retrieve/<int:product_id>', methods=['GET'])
def get_products(product_id):
    return view.get_product(product_id)

# Update a Product
@admin_bp.route('admin/products/update/<int:product_id>', methods=['PUT'])
def update_products(product_id):
    return view.update_product(product_id)

# Delete a Product
@admin_bp.route('/admin/products/delete/<int:product_id>', methods=['DELETE'])
def delete_products(product_id):
    return view.delete_product(product_id)

# Create a Product Variant
@admin_bp.route('/admin/products/product-variants', methods=['POST'])
def create_product_variants():
    return view.create_product_variant()


# Retrieve a Product Variant
@admin_bp.route('/admin/products/product-variants/retrieve/<int:variant_id>', methods=['GET'])
def get_product_variants(variant_id):
    return view.get_product_variant(variant_id)

# Update a Product Variant
@admin_bp.route('/admin/products/product-variants/update/<int:variant_id>', methods=['PUT'])
def update_product_variants(variant_id):
    return view.update_product_variant(variant_id)

# Delete a Product Variant
@admin_bp.route('/admin/products/product-variants/delete/<int:variant_id>', methods=['DELETE'])
def delete_product_variant(variant_id):
    return  view.delete_product_variant(variant_id)


# Create a Category
@admin_bp.route('/admin/products/categories/register', methods=['POST'])
def create_categories():
    return view.create_category()

# Retrieve a Category by ID     
@admin_bp.route('/admin/products/categories/retrieve/<int:category_id>', methods=['GET'])
def get_categories(category_id):
    return view.get_category(category_id)

# Update a Category by ID
@admin_bp.route('/admin/products/categories/update/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    return view.update_category(category_id)

# Delete a Category by ID
@admin_bp.route('/admin/products/categories/delete/<int:category_id>', methods=['DELETE'])
def delete_categories(category_id):
    return view.delete_category(category_id)


# Create a Manufacturer
@admin_bp.route('/admin/products/manufacturers/register', methods=['POST'])
def create_manufacturers():
    return view.create_manufacturer()

# Retrieve all Manufacturers
@admin_bp.route('/admin/products/manufacturers/retrieve', methods=['GET'])
def get_manufacturers():
    return view.get_manufacturers()

# Retrieve a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer(manufacturer_id):
    return view.get_manufacturer(manufacturer_id)

# Update a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/update/<int:manufacturer_id>', methods=['PUT'])
def update_manufacturer(manufacturer_id):
    return view.update_manufacturer(manufacturer_id)

# Delete a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/delete/<int:manufacturer_id>', methods=['DELETE'])
def delete_manufacturer(manufacturer_id):
    return view.delete_manufacturer(manufacturer_id)


@admin_bp.route('/admin/address/register',methods=['POST'])
#@jwt_required()
def addresses_data():
    return view.address_data()

@admin_bp.route('/admin/address/update/<int:address_id>',methods=['PUT']) 
# @jwt_required()
def update_addresses(address_id):
    return view.update_address(address_id)

# Retrieve address
@admin_bp.route('/admin/address/get/<int:address_id>',methods=['get'])
def gets_address(address_id):
    return view.get_address(address_id) 

# Delete
@admin_bp.route('/admin/address/delete/<int:address_id>', methods=['DELETE'])
# @jwt_required()
def delete_addresses(address_id):
    return view.delete_address(address_id)

# Creating a shipping address
@admin_bp.route('/admin/address/shipping_addresses',methods=['POST'])
#  @jwt_required()
def ship_addresses_data():
    return view.shipping_address_data()

# Retrieving a shipping address
@admin_bp.route('/admin/shipping_address/get/<int:address_id>',methods=['get'])
def gets_ship_address(address_id):
    return view.get_ship_address(address_id) 


# Updating a shipping address
@admin_bp.route('/admin/address/shipping_address/update/<int:address_id>',methods=['PUT']) 
#   @jwt_required()
def update_ship_addresses(address_id):
    return view.update_shipping_address(address_id)

# Deleting a shipping address
@admin_bp.route('/admin/address/shipping_address/delete/<int:address_id>', methods=['DELETE'])
#  @jwt_required()
def delete_shipping_addresses(address_id):
    return view.delete_shipping_address(address_id)



# Create a Cart
@admin_bp.route('/admin/carts/create', methods=['POST'])
def create_carts():
    return view.create_cart()

# Retrieve a Cart by ID
@admin_bp.route('/admin/carts/retrieve/<int:cart_id>', methods=['GET'])
def get_carts(cart_id):
    return view.get_cart(cart_id)

# Update a Cart by ID
@admin_bp.route('/admin/carts/update/<int:cart_id>', methods=['PUT'])
def update_carts(cart_id):
    return view.update_cart(cart_id)

# Delete a Cart by ID
@admin_bp.route('/admin/carts/delete/<int:cart_id>', methods=['DELETE'])
def delete_carts(cart_id):
    return view.delete_cart(cart_id)

# Create a Cart Item
@admin_bp.route('/admin/carts/cart_items/create', methods=['POST'])
def create_cart_items():
    return view.create_cart_item()

# Retrieve a Cart Item by ID
@admin_bp.route('/admin/carts/cart_items/retrieve/<int:cart_item_id>', methods=['GET'])
def get_cart_items(cart_item_id):
    return view.get_cart_item(cart_item_id)

# Update a Cart Item by ID
@admin_bp.route('/admin/carts/cart_items/update/<int:cart_item_id>', methods=['PUT'])
def update_cart_items(cart_item_id):
    return view.update_cart_item(cart_item_id)

# Delete a Cart Item by ID
@admin_bp.route('/admin/carts/cart_items/delete/<int:cart_item_id>', methods=['DELETE'])
def delete_cart_item(cart_item_id):
    return view.delete_cart_item(cart_item_id)




# Create a Coupon
@admin_bp.route('/admin/coupons/register', methods=['POST'])
def create_coupon():
    return view.create_coupon()

# Retrieve all Coupons
@admin_bp.route('/admin/coupons/retrieve', methods=['GET'])
def get_coupons():
    return view.get_coupons()


# Retrieve a Coupon by ID
@admin_bp.route('/admin/coupons/retrieve/<int:coupon_id>', methods=['GET'])
def get_coupon():
    return view.get_coupon()

# Update a Coupon by ID
@admin_bp.route('/admin/coupons/update/<int:coupon_id>', methods=['PUT'])
def update_coupon():
    return view.update_coupon()

# Delete a Coupon by ID
@admin_bp.route('/admin/coupons/delete/<int:coupon_id>', methods=['DELETE'])
def delete_coupon():
    return view.delete_coupon()




# Create an Order 
@admin_bp.route('/admin/orders/register', methods=['POST'])
def create_orders():
    return view.create_order()

#Return an order by id
@admin_bp.route('/admin/orders/retrieve/<int:order_id>', methods=['GET'])
def get_orders(order_id):
    return view.get_order(order_id)

# Update an order 
@admin_bp.route('/admin/orders/update/<int:order_id>', methods=['PUT'])
def update_orders(order_id):
    return view.update_order(order_id)

# Delete an Order by ID
@admin_bp.route('/admin/orders/delete/<int:order_id>', methods=['DELETE'])
def delete_orders(order_id):
    return view.delete_order(order_id)

# Create an Order Item
@admin_bp.route('/admin/order-items/register', methods=['POST'])
def create_order_items():
    return view.create_order_item()

# Retrieve an Order Item by ID
@admin_bp.route('/admin/order-items/retrieve/<int:order_item_id>', methods=['GET'])
def get_order_item(order_item_id):
    return view.get_order_item(order_item_id)

# Update an Order Item by ID
@admin_bp.route('/admin/order-items/update/<int:order_item_id>', methods=['PUT'])
def update_order_item(order_item_id):
    return view.update_order_item(order_item_id)

# Delete an Order Item by ID
@admin_bp.route('/admin/order-items/delete/<int:order_item_id>', methods=['DELETE'])
def delete_order_item(order_item_id):
    return view.delete_order_item(order_item_id)

# Create a Payment
@admin_bp.route('/admin/payments/create', methods=['POST'])
def create_payment():
    return view.create_payment()

# Retrieve a Payment by ID
@admin_bp.route('/admin/payments/retrieve/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    return view.get_payment(payment_id)
# Update a Payment by ID
@admin_bp.route('/admin/payments/update/<int:payment_id>', methods=['PUT'])
def update_payments(payment_id):
    view.update_payment(payment_id) 
# Delete a Payment by ID
@admin_bp.route('/admin/payments/delete/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    return view.delete_payment(payment_id)

# Create a Payment Method
@admin_bp.route('/admin/payments/payment_methods/create', methods=['POST'])
def create_payments_method():
    return view.create_payment_method()

# Retrieve a Payment Method by ID
@admin_bp.route('/admin/payments/payment_methods/retrieve/<int:payment_method_id>', methods=['GET'])
def get_payment_method(payment_method_id):
    return view.get_payment_method(payment_method_id)

# Update a Payment Method by ID
@admin_bp.route('/admin/payments/payment_methods/update/<int:payment_method_id>', methods=['PUT'])
def update_payment_method(payment_method_id):
    return view.update_payment_method(payment_method_id)
# Delete a Payment Method by ID
@admin_bp.route('/admin/payments/payment_methods/delete/<int:payment_method_id>', methods=['DELETE'])
def delete_payment_method(payment_method_id):
    return view.delete_payment_method(payment_method_id)
# Create a Transaction
@admin_bp.route('/admin/payments/transactions', methods=['POST'])
def create_transaction():
    return view.create_transaction()

# Retrieve a Transaction by ID
@admin_bp.route('/admin/payments/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    return view.get_transaction(transaction_id)

# Update a Transaction by ID
@admin_bp.route('/admin/payments/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    return view.update_transaction(transaction_id)

# Delete a Transaction by ID
@admin_bp.route('/admin/payments/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    return view.delete_transaction(transaction_id)


# Create a Review
@admin_bp.route('/admin/reviews/register', methods=['POST'])
def create_review():
    return view.create_review()

# Retrieve all Reviews
@admin_bp.route('/admin/reviews/retrieve', methods=['GET'])
def get_reviews():
    return view.get_review()

# Retrieve a Review by ID
@admin_bp.route('/admin/reviews/retrieve/<int:review_id>', methods=['GET'])
def get_review(review_id):
    return view.get_review(review_id)

# Update a Review by ID
@admin_bp.route('/admin/reviews/update/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    return view.update_review(review_id)

# Delete a Review by ID
@admin_bp.route('/admin/reviews/delete/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    return view.delete_review(review_id)



# create a user
@admin_bp.route('admin/user/register', methods=['POST'])
def registers():
        return view.register()

# Getting the user details according to user_id
@admin_bp.route('/admin/user/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    return view.get_user(user_id)

# Getting the list of users
@admin_bp.route('/admin/user/user_retrieval', methods=['GET'])
def get_all_users_route():
    return view.get_all_users()


# Update
@admin_bp.route('/admin/user/update/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    return view.update_user(user_id)
# Delete
@admin_bp.route('/admin/user/delete/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return view.delete_user(user_id)

# Retrieve all Category      
@admin_bp.route('products/categories/retrieve', methods=['GET'])
def get_all_categories():
    return view.get_all_categories()

