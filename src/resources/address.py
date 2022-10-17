from flask_restful import Resource
from models.address import AddressModel
from utils.generate_address import generate_address

class Addresses(Resource):
    def get(self):
        return {'addresses': [address.json() for address in AddressModel.query.all()]}


class Address(Resource):
    def get(self, crypto, address_id):
        address = AddressModel.find_address(address_id)

        if address:
            return address.json()

        return {
            "message": "Address not found",
        }, 404  # not found

    def post(self, crypto):
        _crypto = crypto.upper()
        _address = generate_address(_crypto)

        new_address = AddressModel(
            crypto = _crypto,
            address = _address
        )

        try:
            new_address.save_address()
        except Exception as error:
            print(str(error))
            return {"message": "An error ocurred trying to create address."}, 500 #Internal Server Error
        
        return new_address.json(), 201
