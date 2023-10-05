from flask import request, jsonify
from datetime import datetime
from e_commerce.db import db
#from e_commerce.app import db
from e_commerce.product.models import Products,ProductVariants,Categories,Manufacturers

def create_product():
    try:
        data = request.json
        new_product = Products(
                        product_id=data['product_id'],
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
    
def product_to_dict(product):
    return {
        'product_id': product.product_id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock_quantity': product.stock_quantity,
        'category_id': product.category_id,
        'image_url': product.image_url,
        'manufacturer_id': product.manufacturer_id,
        'creation_date': product.creation_date,
        'average_rating': product.average_rating,
        'total_ratings': product.total_ratings
    }    
    
# Retrieves product data
def get_product(product_id):
        product = Products.query.get(product_id)
        if product:
            product_dict = product_to_dict(product)
            return jsonify(product_dict), 200
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
        return jsonify({ "variant_id":variant.variant_id,
    "product_id": variant.product_id,
    "color": variant.color,
    "size": variant.size,
    "material": variant.material,
    "other_features":variant.other_features,
    "specification": variant.specification,
    "image_url": variant.image_url,
    "price": variant.price,
    "quantity":variant.quantity,
    "created_at": variant.created_at}), 200
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

# Create a Category
def create_category():
    try:
        data = request.json
        new_category = Categories(
            name=data['name']
        )
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message': 'Category created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve a Category by ID
def get_category(category_id):
    category = Categories.query.get(category_id)
    if category:
        return jsonify(   { "category_id":category.category_id,
    "name":category.name}), 200
    else:
        return jsonify({'message': 'Category not found'}), 404
    
# Update a Category by ID
def update_category(category_id):
    category = Categories.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404

    data = request.json
    category.name = data.get('name', category.name)

    db.session.commit()
    return jsonify({'message': 'Category updated successfully'}), 200

# Delete a Category by ID
def delete_category(category_id):
    category = Categories.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'}), 200

# Create a Manufacturer
def create_manufacturer():
    try:
        data = request.json
        new_manufacturer = Manufacturers(
            name=data['name'],
            country=data['country']
        )
        db.session.add(new_manufacturer)
        db.session.commit()
        return jsonify({'message': 'Manufacturer created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Retrieve all Manufacturers
def get_manufacturers():
    manufacturers = Manufacturers.query.all()
    manufacturer_list = [{'manufacturer_id': manufacturer.manufacturer_id,
                            'name': manufacturer.name} for manufacturer in manufacturers]
    return jsonify(manufacturer_list), 200


# Retrieve a Manufacturer by ID
def get_manufacturer(manufacturer_id):
    manufacturer = Manufacturers.query.get(manufacturer_id)
    if manufacturer:
        return jsonify({'manufacturer_id': manufacturer.manufacturer_id,
                            'name': manufacturer.name}), 200
    else:
        return jsonify({'message': 'Manufacturer not found'}), 404
# Update a Manufacturer by ID
def update_manufacturer(manufacturer_id):
    manufacturer = Manufacturers.query.get(manufacturer_id)
    if not manufacturer:
        return jsonify({'message': 'Manufacturer not found'}), 404

    data = request.json
    manufacturer.name = data.get('name', manufacturer.name)
    manufacturer.country = data.get('country', manufacturer.country)

    db.session.commit()
    return jsonify({'message': 'Manufacturer updated successfully'}), 200

# Delete a Manufacturer by ID
def delete_manufacturer(manufacturer_id):
    manufacturer = Manufacturers.query.get(manufacturer_id)
    if not manufacturer:
        return jsonify({'message': 'Manufacturer not found'}), 404

    db.session.delete(manufacturer)
    db.session.commit()
    return jsonify({'message': 'Manufacturer deleted successfully'}), 200
    