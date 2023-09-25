from flask_jwt_extended import jwt_required
from e_commerce.product import view
from flask import Blueprint

product_bp = Blueprint('products', __name__)


# Create a Product
@product_bp.route('/products/register', methods=['POST'])
def create_products():
    return view.create_product()

# Retrieve a Product
@product_bp.route('/products/retrieve/<int:product_id>', methods=['GET'])
def get_products():
    return view.get_product()

# Update a Product
@product_bp.route('/products/update/<int:product_id>', methods=['PUT'])
def update_products():
    return view.update_product()
# Delete a Product
@product_bp.route('/products/delete/<int:product_id>', methods=['DELETE'])
def delete_products():
    return view.delete_product()

# Create a Product Variant
@product_bp.route('/products/product-variants', methods=['POST'])
def create_product_variants():
    return view.create_product_variant()

# Retrieve a Product Variant
@product_bp.route('/products/product-variants/retrieve/<int:variant_id>', methods=['GET'])
def get_product_variants():
    return view.get_product_variant()

# Update a Product Variant
@product_bp.route('products/product-variants/update/<int:variant_id>', methods=['PUT'])
def update_product_variants():
    return view.update_product_variant()
# Delete a Product Variant
@product_bp.route('products/product-variants/delete/<int:variant_id>', methods=['DELETE'])
def delete_product_variant():
    return  view.delete_product_variant()

# Create a Category
@product_bp.route('products/categories/register', methods=['POST'])
def create_categories():
    return view.create_category()

# Retrieve a Category by ID
@product_bp.route('products/categories/retrieve/<int:category_id>', methods=['GET'])
def get_categories():
    return view.get_category()

# Update a Category by ID
@product_bp.route('products/categories/update/<int:category_id>', methods=['PUT'])
def update_category():
    return view.update_category()

# Delete a Category by ID
@product_bp.route('products/categories/delete/<int:category_id>', methods=['DELETE'])
def delete_categories():
    return view.delete_category()

# Create a Manufacturer
@product_bp.route('/products/manufacturers/register', methods=['POST'])
def create_manufacturers():
    return view.create_manufacturer()

# Retrieve all Manufacturers
@product_bp.route('/products/manufacturers/retrieve', methods=['GET'])
def get_manufacturers():
    return view.get_manufacturers()

# Retrieve a Manufacturer by ID
@product_bp.route('products/manufacturers/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer():
    return view.get_manufacturer()

# Update a Manufacturer by ID
@product_bp.route('products/manufacturers/<int:manufacturer_id>', methods=['PUT'])
def update_manufacturer():
    return view.update_manufacturer()

# Delete a Manufacturer by ID
@product_bp.route('products/manufacturers/<int:manufacturer_id>', methods=['DELETE'])
def delete_manufacturer():
    return view.delete_manufacturer()