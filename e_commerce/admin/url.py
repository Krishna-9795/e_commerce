
#from e_commerce.utils import admin_token
from e_commerce.admin import view
from e_commerce.product.view import get_product,update_product,delete_product,create_product_variant,get_product_variant,get_category,update_category
from e_commerce.product.view import create_manufacturer,create_product,update_product_variant,delete_product_variant,delete_category,create_category,get_manufacturers,get_manufacturer,update_manufacturer,delete_manufacturer
from e_commerce.addresses.view import delete_shipping_address, update_shipping_address, get_ship_address, shipping_address_data, delete_address, get_address, update_address, address_data
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/register',methods=['POST'])
def admin_reg():
    return view.admin_register()

@admin_bp.route('/admin/login/' , methods = ['POST'])
def admin_login():
    return view.admin_login()

@admin_bp.route('/admin/product/create',methods=['POST'])
def admin_prod_create():
    return create_product()

@admin_bp.route('admin/products/retrieve/<int:product_id>', methods=['GET'])
def get_products(product_id):
    return get_product(product_id)

# Update a Product
@admin_bp.route('admin/products/update/<int:product_id>', methods=['PUT'])
def update_products(product_id):
    return update_product(product_id)

# Delete a Product
@admin_bp.route('/admin/products/delete/<int:product_id>', methods=['DELETE'])
def delete_products(product_id):
    return delete_product(product_id)

# Create a Product Variant
@admin_bp.route('/admin/products/product-variants', methods=['POST'])
def create_product_variants():
    return create_product_variant()


# Retrieve a Product Variant
@admin_bp.route('/admin/products/product-variants/retrieve/<int:variant_id>', methods=['GET'])
def get_product_variants(variant_id):
    return get_product_variant(variant_id)

# Update a Product Variant
@admin_bp.route('/admin/products/product-variants/update/<int:variant_id>', methods=['PUT'])
def update_product_variants(variant_id):
    return update_product_variant(variant_id)

# Delete a Product Variant
@admin_bp.route('/admin/products/product-variants/delete/<int:variant_id>', methods=['DELETE'])
def delete_product_variant(variant_id):
    return  delete_product_variant(variant_id)


# Create a Category
@admin_bp.route('/admin/products/categories/register', methods=['POST'])
def create_categories():
    return create_category()

# Retrieve a Category by ID     
@admin_bp.route('/admin/products/categories/retrieve/<int:category_id>', methods=['GET'])
def get_categories(category_id):
    return get_category(category_id)

# Update a Category by ID
@admin_bp.route('/admin/products/categories/update/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    return update_category(category_id)

# Delete a Category by ID
@admin_bp.route('/admin/products/categories/delete/<int:category_id>', methods=['DELETE'])
def delete_categories(category_id):
    return delete_category(category_id)


# Create a Manufacturer
@admin_bp.route('/admin/products/manufacturers/register', methods=['POST'])
def create_manufacturers():
    return create_manufacturer()

# Retrieve all Manufacturers
@admin_bp.route('/admin/products/manufacturers/retrieve', methods=['GET'])
def get_manufacturers():
    return get_manufacturers()

# Retrieve a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer(manufacturer_id):
    return get_manufacturer(manufacturer_id)

# Update a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/update/<int:manufacturer_id>', methods=['PUT'])
def update_manufacturer(manufacturer_id):
    return update_manufacturer(manufacturer_id)

# Delete a Manufacturer by ID
@admin_bp.route('/admin/manufacturers/delete/<int:manufacturer_id>', methods=['DELETE'])
def delete_manufacturer(manufacturer_id):
    return delete_manufacturer(manufacturer_id)


@admin_bp.route('/address/register',methods=['POST'])
#@jwt_required()
def addresses_data():
    return address_data()

@admin_bp.route('/address/update/<int:address_id>',methods=['PUT']) 
# @jwt_required()
def update_addresses(address_id):
    return update_address(address_id)

# Retrieve address
@admin_bp.route('/address/get/<int:address_id>',methods=['get'])
def gets_address(address_id):
    return get_address(address_id) 

# Delete
@admin_bp.route('/address/delete/<int:address_id>', methods=['DELETE'])
# @jwt_required()
def delete_addresses(address_id):
    return delete_address(address_id)

# Creating a shippping address
@admin_bp.route('/address/shipping_addresses',methods=['POST'])
#  @jwt_required()
def ship_addresses_data():
    return shipping_address_data()

# Retrieving a shipping address
@admin_bp.route('/shipping_address/get/<int:address_id>',methods=['get'])
def gets_ship_address(address_id):
    return get_ship_address(address_id) 


# Updating a shipping address
@admin_bp.route('/address/shipping_address/update/<int:address_id>',methods=['PUT']) 
#   @jwt_required()
def update_ship_addresses(address_id):
    return update_shipping_address(address_id)

# Deleting a shipping address
@admin_bp.route('/address/shipping_address/delete/<int:address_id>', methods=['DELETE'])
#  @jwt_required()
def delete_shipping_addresses(address_id):
    return delete_shipping_address(address_id)


from e_commerce.carts import view
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