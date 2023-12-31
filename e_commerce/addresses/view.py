from flask import request, jsonify

from addresses.models import Addresses,ShippingAddresses
from e_commerce.db import db

# Creating a record
def address_data():
    data = request.get_json()
    
    # Check if required fields are present in the JSON data
    if 'user_id' not in data or 'street_address' not in data:
        return jsonify({'message': 'user ID and Street Address are required fields'}), 400

    else:
        new_address = Addresses(
            user_id=data['user_id'],
            street_address=data['street_address'],
            city=data.get('city'),
            state=data.get('state'),
            postal_code=data.get('postal_code'),
            country=data.get('country'),
            is_default=data.get('is_default', False)  # Provide a default value if not present
        )
        db.session.add(new_address)
        db.session.commit()
        return jsonify({'message': 'New address record created'}), 201  # 201 indicates resource created

#retrieving a record of address
def get_address(address_id):
    address=Addresses.query.get(address_id)
    address_data=[]
    if  address is None:
            return jsonify({'message': 'address not found'})
    else :
        address_data.append({
            'address_id':address.address_id,
            'user_id':address.user_id,
            'street_address':address.street_address,
            'city':address.city,
            'state':address.state,
            'postal_code':address.postal_code,
            'country':address.country,
            'is_default':address.is_default       
        })
    return jsonify({'address': address_data}),200

        
# Updating a record
def update_address(address_id):
        data = request.get_json()
        address = Addresses.query.get(address_id)
        if not address:
            return jsonify({'message': 'address not found'})

        address.address_id=data.get('address_id',address.address_id)
        address.street_address=data.get('street_address',address.address_id)
        address.city=data.get('city',address.city)
        address.state=data.get('state',address.state)
        address.postal_code=data.get('postal_code',address.postal_code)
        address.country=data.get('country',address.country)
        address.is_default=data.get('is_default',address.is_default)
        db.session.commit()

        return jsonify({'message': 'Address updated successfully'})
    
# Deleting a address record
def delete_address(address_id):
    
    address = Addresses.query.get(address_id)

    if not address:
        return jsonify({'message': 'Address not found'})

    db.session.delete(address)
    db.session.commit()

    return jsonify({'message': 'Address deleted successfully'})

# Creating a shipping_address record
def shipping_address_data():
    data=request.get_json()
    new_address=ShippingAddresses(address_id=data['address_id'], street_address=data['street_address'],
                city=data['city'], state=data['state'], postal_code=data['postal_code'],
                country=data['country'] )
    db.session.add(new_address)
    db.session.commit()
    return jsonify({'message':'New address record created'})

# Retrieving a shipping address
def get_ship_address(address_id):
    address=ShippingAddresses.query.get(address_id)
    address_data=[]
    if  address is None:
            return jsonify({'message': 'address not found'})
    else :
        address_data.append({
            'address_id':address.address_id,
            'user_id':address.user_id,
            'street_address':address.street_address,
            'city':address.city,
            'state':address.state,
            'postal_code':address.postal_code,
            'country':address.country     
        })
    return jsonify({'address': address_data}),200

def update_shipping_address(address_id):
        data = request.get_json()
        shipping_address = ShippingAddresses.query.get(address_id)
        if not shipping_address:
            return jsonify({'message': 'address not found'})

        shipping_address.address_id=data.get('address_id',shipping_address.address_id)
        shipping_address.street_address=data.get('street_address',shipping_address.address_id)
        shipping_address.city=data.get('city',shipping_address.city)
        shipping_address.state=data.get('state',shipping_address.state)
        shipping_address.postal_code=data.get('postal_code',shipping_address.postal_code)
        shipping_address.country=data.get('country',shipping_address.country)
        db.session.commit()

        return jsonify({'message': 'Shipping Address updated successfully'})
    
def delete_shipping_address(address_id):
    
    shipping_address = ShippingAddresses.query.get(address_id)

    if not shipping_address:
        return jsonify({'message': 'Address not found'})

    db.session.delete(shipping_address)
    db.session.commit()

    return jsonify({'message': 'Address deleted successfully'})
