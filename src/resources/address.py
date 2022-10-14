from flask_restful import Resource, reqparse
from models.address import AddressModel

class Addresses(Resource):
    def get(self):
        return {'addresses': [address.json() for address in AddressModel.query.all()]}


class Address(Resource):
    attributes = reqparse.RequestParser()
    attributes.add_argument("crypto")
    attributes.add_argument("address")

    def get(self, address_id):
        address = Address.find_address(address_id)

        if address:
            return address

        return {
            "message": "Address not found",
        }, 404  # not found

    def post(self):
        data = Address.attributes.parse_args()

        new_address = AddressModel(
            **data,
        )

        print(new_address.json())

        try:
            new_address.save_address()
        except Exception as error:
            print(str(error))
            return {"message": "An error ocurred trying to create address."}, 500 #Internal Server Error
        
        return new_address.json(), 201
