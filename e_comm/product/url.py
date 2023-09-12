from e_comm.app import app
from flask_jwt_extended import jwt_required
from product.view import create_product,get_product, update_product,delete_product,create_product_variant,get_product_variant,update_product_variant,delete_product_variant

from flask_sqlalchemy import SQLAlchemy



# Create a Product
@app.route('/products', methods=['POST'])
def create_products():
    return create_product()

# Retrieve a Product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_products():
    return get_product()

# Update a Product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_products():
    return update_product()
# Delete a Product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_products():
    return delete_product()

# Create a Product Variant
@app.route('/product-variants', methods=['POST'])
def create_product_variants():
    return create_product_variant()

# Retrieve a Product Variant
@app.route('/product-variants/<int:variant_id>', methods=['GET'])
def get_product_variants():
    return get_product_variant()

# Update a Product Variant
@app.route('/product-variants/<int:variant_id>', methods=['PUT'])
def update_product_variants():
    return update_product_variant()
# Delete a Product Variant
@app.route('/product-variants/<int:variant_id>', methods=['DELETE'])
def delete_product_variant():
    return  delete_product_variant()
