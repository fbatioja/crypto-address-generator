from flask_restful import Resource, reqparse
from models.address import AddressModel
from utils.generate_address import generate_address

class Addresses(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument("private_key")

    def get(self, crypto):
        _crypto = crypto.upper()

        return {'addresses': [address.json() for address in AddressModel.find_address_by_crypto(_crypto)]}
    
    def post(self, crypto):
        data = Addresses.arguments.parse_args()

        private_key = data['private_key']

        _crypto = crypto.upper()
        _address = generate_address(_crypto, private_key)

        if not _address:
            return {
                "message": "Crypto not available",
            }, 400

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


class Address(Resource):
    def get(self, crypto, address_id):
        _crypto = crypto.upper()

        address = AddressModel.find_address(address_id, _crypto)

        if address:
            return address.json()

        return {
            "message": "Address not found",
        }, 404  # not found