from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from e_comm.app import db
from e_comm.product.models import Products,ProductVariants

def create_product():
    try:
        data = request.json
        new_product = Products(
                        name=data['name'],
                        description=data['description'],
                        price=data['price'],
                        stock_quantity=data['stock_quantity'],
                        category_id=data['category_id'],
                        image_url=data['image_url'],
                        manufacturer_id=data.get('manufacturer_id'),
                        creation_date=str(datetime.utcnow()),
                        average_rating=data.get('average_rating'),
                        total_ratings=data.get('total_ratings'))
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Retrieves product data
def get_product(product_id):
    product = Products.query.get(product_id)
    if product:
        return jsonify(product.serialize()), 200
    else:
        return jsonify({'message': 'Product not found'}), 404
    
# Updates product data
def update_product(product_id):
    product = Products.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    data = request.json
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
    product.category_id = data.get('category_id', product.category_id)
    product.image_url = data.get('image_url', product.image_url)
    product.manufacturer_id = data.get('manufacturer_id', product.manufacturer_id)
    product.creation_date = data.get('creation_date', product.creation_date)
    product.average_rating = data.get('average_rating', product.average_rating)
    product.total_ratings = data.get('total_ratings', product.total_ratings)

    db.session.commit()
    return jsonify({'message': 'Product updated successfully'}), 200
#delete product record
def delete_product(product_id):
    product = Products.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

# Create a product variant
def create_product_variant():
    try:
        data = request.json
        new_variant = ProductVariants(
            product_id=data['product_id'],
            color=data.get('color'),
            size=data.get('size'),
            material=data.get('material'),
            other_features=data.get('other_features'),
            specification=data.get('specification'),
            image_url=data.get('image_url'),
            price=data['price'],
            quantity=data['quantity'],
            created_at=datetime.utcnow()
        )
        db.session.add(new_variant)
        db.session.commit()
        return jsonify({'message': 'Product variant created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Retrieve a ProductVariant
def get_product_variant(variant_id):
    variant = ProductVariants.query.get(variant_id)
    if variant:
        return jsonify(variant.serialize()), 200
    else:
        return jsonify({'message': 'Product variant not found'}), 404
    
# Update a Product Variant
def update_product_variant(variant_id):
    variant = ProductVariants.query.get(variant_id)
    if not variant:
        return jsonify({'message': 'Product variant not found'}), 404

    data = request.json
    variant.product_id = data.get('product_id', variant.product_id)
    variant.color = data.get('color', variant.color)
    variant.size = data.get('size', variant.size)
    variant.material = data.get('material', variant.material)
    variant.other_features = data.get('other_features', variant.other_features)
    variant.specification = data.get('specification', variant.specification)
    variant.image_url = data.get('image_url', variant.image_url)
    variant.price = data.get('price', variant.price)
    variant.quantity = data.get('quantity', variant.quantity)

    db.session.commit()
    return jsonify({'message': 'Product variant updated successfully'}), 200

# Deleting a Product Variant
def delete_product_variant(variant_id):
    variant = ProductVariants.query.get(variant_id)
    if not variant:
        return jsonify({'message': 'Product variant not found'}), 404

    db.session.delete(variant)
    db.session.commit()
    return jsonify({'message': 'Product variant deleted successfully'}), 200


