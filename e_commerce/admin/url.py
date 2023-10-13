from e_commerce.utils import admin_token
from e_commerce.admin import view 
from e_commerce.product.view import create_product,get_product,update_product,delete_product,create_product_variant,get_product_variant,update_product_variant,delete_product_variant,create_category,get_category,update_category,delete_category,create_manufacturer,get_manufacturers,get_manufacturer,update_manufacturer,delete_manufacturer,get_all_products
from e_commerce.addresses.view import address_data,update_address,get_address,delete_address,shipping_address_data,get_ship_address,update_shipping_address,delete_shipping_address
from e_commerce.carts.view import create_cart,get_cart,update_cart,delete_cart,create_cart_item,get_cart_item,update_cart_item,delete_cart_item
from e_commerce.orders.view import create_order,get_order,update_order,delete_order,create_order_item,get_order_item,update_order_item,delete_order_item
from e_commerce.coupons.view import create_coupon,get_coupons,get_coupon,update_coupon,delete_coupon
from e_commerce.payments.view import create_payment,get_payment,update_payment,delete_payment,create_payment_method,get_payment_method,update_payment_method,delete_payment_method,create_transaction,get_transaction,update_transaction,delete_transaction
from e_commerce.user.view  import register,get_user,get_all_users,update_user,delete_user
from e_commerce.review.view import create_review,get_review,get_review,update_review,delete_review
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)



from e_commerce.admin import view
# Register admin
@admin_bp.route('/admin/register',methods=['POST'])
def admin_reg():
    return view.admin_register()
# admin login
@admin_bp.route('/admin/login/' , methods = ['POST'])
def admin_login():
    return view.admin_login()
# Get admin
@admin_bp.route('/admin/get/<int:id>' , methods = ['GET'])
@admin_token
def get_admin(id):
    return view.get_admin(id)
# Admin update
@admin_bp.route('/admin/update/<int:id>' , methods = ['PUT'])
@admin_token
def update_admin(id):
    return view.update_admin(id)
# Deleting admin
@admin_bp.route('/admin/delete/<int:id>' , methods = ['DELETE'])
@admin_token
def delete_admin(id):
    return view.delete_admin(id)

# Create a product record
@admin_bp.route('/admin/product/create',methods=['POST'])
@admin_token
def admin_prod_create():
    return create_product()
# Get product by id
@admin_bp.route('admin/products/retrieve/<int:product_id>', methods=['GET'])
@admin_token
def get_products(product_id):
    return get_product(product_id)
# Get all product
@admin_bp.route('admin/products/retrieve', methods=['GET'])
@admin_token
def get_all_product_route():
    return get_all_products()

# Update a Product
@admin_bp.route('admin/products/update/<int:product_id>', methods=['PUT'])
@admin_token
def update_products(product_id):
    return update_product(product_id)

# Delete a Product
@admin_bp.route('/admin/products/delete/<int:product_id>', methods=['DELETE'])
@admin_token
def delete_products(product_id):
    return delete_product(product_id)

# Create a Product Variant
@admin_bp.route('/admin/products/product-variants', methods=['POST'])
@admin_token
def create_product_variants():
    return create_product_variant()


# Retrieve a Product Variant
@admin_bp.route('/admin/products/product-variants/retrieve/<int:variant_id>', methods=['GET'])
@admin_token
def get_product_variants(variant_id):
    return get_product_variant(variant_id)

# Update a Product Variant
@admin_bp.route('/admin/products/product-variants/update/<int:variant_id>', methods=['PUT'])
@admin_token
def update_product_variants(variant_id):
    return update_product_variant(variant_id)

# Delete a Product Variant
@admin_bp.route('/admin/products/product-variants/delete/<int:variant_id>', methods=['DELETE'])
@admin_token
def delete_product_variant_route(variant_id):
    return  delete_product_variant(variant_id)

# Create a Category
@admin_bp.route('/admin/products/categories/register', methods=['POST'])
@admin_token
def create_categories():
    return create_category()

# Retrieve a Category by ID     
@admin_bp.route('/admin/products/categories/retrieve/<int:category_id>', methods=['GET'])
@admin_token
def get_categories(category_id):
    return get_category(category_id)

# Update a Category by ID
@admin_bp.route('/admin/products/categories/update/<int:category_id>', methods=['PUT'])
@admin_token
def update_category_route(category_id):
    return update_category(category_id)

# Delete a Category by ID
@admin_bp.route('/admin/products/categories/delete/<int:category_id>', methods=['DELETE'])
@admin_token
def delete_categories(category_id):
    return delete_category(category_id)


# Create a Manufacturer
@admin_bp.route('/admin/products/manufacturers/register', methods=['POST'])
@admin_token
def create_manufacturers():
    return create_manufacturer()

# Retrieve all Manufacturers
@admin_bp.route('/admin/products/manufacturers/retrieve', methods=['GET'])
@admin_token
def get_manufacturers_route():
    return get_manufacturers()

# Retrieve a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/<int:manufacturer_id>', methods=['GET'])
@admin_token
def get_manufacturer_route(manufacturer_id):
    return get_manufacturer(manufacturer_id)

# Update a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/update/<int:manufacturer_id>', methods=['PUT'])
@admin_token
def update_manufacturer_route(manufacturer_id):
    return  update_manufacturer(manufacturer_id)

# Delete a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/delete/<int:manufacturer_id>', methods=['DELETE'])
@admin_token
def delete_manufacturer_route(manufacturer_id):
    return delete_manufacturer(manufacturer_id)

# Create register
@admin_bp.route('/admin/address/register',methods=['POST'])
@admin_token
def addresses_data():
    return address_data()
# Updating address
@admin_bp.route('/admin/address/update/<int:address_id>',methods=['PUT']) 
@admin_token
def update_addresses(address_id):
    return update_address(address_id)

# Retrieve address
@admin_bp.route('/admin/address/get/<int:address_id>',methods=['get'])
@admin_token
def gets_address(address_id):
    return get_address(address_id) 

# Delete
@admin_bp.route('/admin/address/delete/<int:address_id>', methods=['DELETE'])
@admin_token
def delete_addresses(address_id):
    return delete_address(address_id)

# Creating a shipping address
@admin_bp.route('/admin/address/shipping_addresses',methods=['POST'])
@admin_token
def ship_addresses_data():
    return shipping_address_data()


# Retrieving a shipping address
@admin_bp.route('/admin/shipping_address/get/<int:address_id>',methods=['get'])
@admin_token
def gets_ship_address_route(address_id):
    return get_ship_address(address_id) 

# Updating a shipping address
@admin_bp.route('/admin/address/shipping_address/update/<int:address_id>',methods=['PUT']) 
@admin_token
def update_ship_addresses(address_id):
    return update_shipping_address(address_id)

# Deleting a shipping address
@admin_bp.route('/admin/address/shipping_address/delete/<int:address_id>', methods=['DELETE'])
@admin_token
def delete_shipping_address_route(address_id):
    return delete_shipping_address(address_id)

# Create a Cart
@admin_bp.route('/admin/carts/create', methods=['POST'])
@admin_token
def create_carts():
    return create_cart()

# Retrieve a Cart by ID
@admin_bp.route('/admin/carts/retrieve/<int:cart_id>', methods=['GET'])
@admin_token
def get_cart_route(cart_id):
    return get_cart(cart_id)

# Update a Cart by ID
@admin_bp.route('/admin/carts/update/<int:cart_id>', methods=['PUT'])
@admin_token
def update_carts(cart_id):
    return update_cart(cart_id)

# Delete a Cart by ID
@admin_bp.route('/admin/carts/delete/<int:cart_id>', methods=['DELETE'])
@admin_token
def delete_carts(cart_id):
    return delete_cart(cart_id)

# Create a Cart Item
@admin_bp.route('/admin/carts/cart_items/create', methods=['POST'])
@admin_token
def create_cart_items():
    return create_cart_item()

# Retrieve a Cart Item by ID
@admin_bp.route('/admin/carts/cart_items/retrieve/<int:cart_item_id>', methods=['GET'])
@admin_token
def get_cart_items(cart_item_id):
    return get_cart_item(cart_item_id)

# Update a Cart Item by ID
@admin_bp.route('/admin/carts/cart_items/update/<int:cart_item_id>', methods=['PUT'])
@admin_token
def update_cart_items(cart_item_id):
    return update_cart_item(cart_item_id)

# Delete a Cart Item by ID
@admin_bp.route('/admin/carts/cart_items/delete/<int:cart_item_id>', methods=['DELETE'])
@admin_token
def delete_cart_item_route(cart_item_id):
    return delete_cart_item(cart_item_id)



# Create a Coupon
@admin_bp.route('/admin/coupons/register', methods=['POST'])
@admin_token
def create_coupon_route():
    return create_coupon()

# Retrieve all Coupons
@admin_bp.route('/admin/coupons/retrieve', methods=['GET'])
@admin_token
def get_coupons_route():
    return get_coupons()

# Retrieve a Coupon by ID
@admin_bp.route('/admin/coupons/retrieve/<int:coupon_id>', methods=['GET'])
@admin_token
def get_coupon_route():
    return get_coupon()

# Update a Coupon by ID
@admin_bp.route('/admin/coupons/update/<int:coupon_id>', methods=['PUT'])
@admin_token
def update_coupon_route():
    return update_coupon()

# Delete a Coupon by ID
@admin_bp.route('/admin/coupons/delete/<int:coupon_id>', methods=['DELETE'])
@admin_token
def delete_coupon_route():
    return delete_coupon()


# Create an Order 
@admin_bp.route('/admin/orders/register', methods=['POST'])
@admin_token
def create_orders_route():
    return create_order()

#Return an order by id
@admin_bp.route('/admin/orders/retrieve/<int:order_id>', methods=['GET'])
@admin_token
def get_orders_route(order_id):
    return get_order(order_id)

# Update an order 
@admin_bp.route('/admin/orders/update/<int:order_id>', methods=['PUT'])
@admin_token
def update_orders_route(order_id):
    return update_order(order_id)

# Delete an Order by ID
@admin_bp.route('/admin/orders/delete/<int:order_id>', methods=['DELETE'])
@admin_token
def delete_orders_route(order_id):
    return delete_order(order_id)

# Create an Order Item
@admin_bp.route('/admin/order-items/register', methods=['POST'])
@admin_token
def create_order_items_route():
    return create_order_item()

# Retrieve an Order Item by ID
@admin_bp.route('/admin/order-items/retrieve/<int:order_item_id>', methods=['GET'])
@admin_token
def get_order_item_route(order_item_id):
    return get_order_item(order_item_id)

# Update an Order Item by ID
@admin_bp.route('/admin/order-items/update/<int:order_item_id>', methods=['PUT'])
@admin_token
def update_order_item_route(order_item_id):
    return update_order_item(order_item_id)

# Delete an Order Item by ID
@admin_bp.route('/admin/order-items/delete/<int:order_item_id>', methods=['DELETE'])
@admin_token
def delete_order_item_route(order_item_id):
    return delete_order_item(order_item_id)



# Create a Payment
@admin_bp.route('/admin/payments/create', methods=['POST'])
@admin_token
def create_payment_route():
    return create_payment()

# Retrieve a Payment by ID
@admin_bp.route('/admin/payments/retrieve/<int:payment_id>', methods=['GET'])
@admin_token
def get_payment_route(payment_id):
    return get_payment(payment_id)
# Update a Payment by ID
@admin_bp.route('/admin/payments/update/<int:payment_id>', methods=['PUT'])
@admin_token
def update_payments_route(payment_id):
    return update_payment(payment_id) 
# Delete a Payment by ID
@admin_bp.route('/admin/payments/delete/<int:payment_id>', methods=['DELETE'])
@admin_token
def delete_payment_route(payment_id):
    return delete_payment(payment_id)

# Create a Payment Method
@admin_bp.route('/admin/payments/payment_methods/create', methods=['POST'])
@admin_token
def create_payments_method():
    return create_payment_method()

# Retrieve a Payment Method by ID
@admin_bp.route('/admin/payments/payment_methods/retrieve/<int:payment_method_id>', methods=['GET'])
@admin_token
def get_payment_method_route(payment_method_id):
    return get_payment_method(payment_method_id)

# Update a Payment Method by ID
@admin_bp.route('/admin/payments/payment_methods/update/<int:payment_method_id>', methods=['PUT'])
@admin_token
def update_payment_method_route(payment_method_id):
    return update_payment_method(payment_method_id)
# Delete a Payment Method by ID
@admin_bp.route('/admin/payments/payment_methods/delete/<int:payment_method_id>', methods=['DELETE'])
@admin_token
def delete_payment_method_route(payment_method_id):
    return delete_payment_method(payment_method_id)
# Create a Transaction
@admin_bp.route('/admin/payments/transactions', methods=['POST'])
@admin_token
def create_transaction_route():
    return create_transaction()

# Retrieve a Transaction by ID
@admin_bp.route('/admin/payments/transactions/<int:transaction_id>', methods=['GET'])
@admin_token
def get_transaction_route(transaction_id):
    return get_transaction(transaction_id)

# Update a Transaction by ID
@admin_bp.route('/admin/payments/transactions/<int:transaction_id>', methods=['PUT'])
@admin_token
def update_transaction_route(transaction_id):
    return update_transaction(transaction_id)

# Delete a Transaction by ID
@admin_bp.route('/admin/payments/transactions/<int:transaction_id>', methods=['DELETE'])
@admin_token
def delete_transaction_route(transaction_id):
    return delete_transaction(transaction_id)

# Create a Review
@admin_bp.route('/admin/reviews/register', methods=['POST'])
@admin_token
def create_review_route():
    return create_review()

# Retrieve all Reviews
@admin_bp.route('/admin/reviews/retrieve', methods=['GET'])
@admin_token
def get_reviews_route():
    return get_review()

# Retrieve a Review by ID
@admin_bp.route('/admin/reviews/retrieve/<int:review_id>', methods=['GET'])
@admin_token
def get_review_route(review_id):
    return get_review(review_id)

# Update a Review by ID
@admin_bp.route('/admin/reviews/update/<int:review_id>', methods=['PUT'])
@admin_token
def update_review_route(review_id):
    return update_review(review_id)

# Delete a Review by ID
@admin_bp.route('/admin/reviews/delete/<int:review_id>', methods=['DELETE'])
@admin_token
def delete_review_route(review_id):
    return delete_review(review_id)


# create a user
@admin_bp.route('admin/user/register', methods=['POST'])
@admin_token
def registers():
        return register()

# Getting the user details according to user_id
@admin_bp.route('/admin/user/users/<int:user_id>', methods=['GET'])
@admin_token
def get_user_route(user_id):
    return get_user(user_id)

# Getting the list of users
@admin_bp.route('/admin/user/user_retrieval', methods=['GET'])
@admin_token
def get_all_users_route():
    return get_all_users()

# Update
@admin_bp.route('/admin/user/update/<int:user_id>', methods=['PUT'])
@admin_token
def update_user_route(user_id):
    return update_user(user_id)
# Delete
@admin_bp.route('/admin/user/delete/<int:user_id>', methods=['DELETE'])
@admin_token
def delete_user_route(user_id):
    return delete_user(user_id)





