from flask_restful import Resource, reqparse
from models.crypto import CryptoModel

class Cryptos(Resource):
    def get(self):
        return {'cryptos': [crypto.json() for crypto in CryptoModel.query.all()]}


class Crypto(Resource):
    attributes = reqparse.RequestParser()
    attributes.add_argument("crypto")

    def get(self, crypto_id):
        crypto = CryptoModel.find_crypto(crypto_id)

        if crypto:
            return crypto.json()

        return {
            "message": "crypto not found",
        }, 404  # not found

    def post(self):
        data = Crypto.attributes.parse_args()

        print(data)

        _crypto = data.crypto.upper()

        new_crypto = CryptoModel(
            crypto = _crypto
        )

        try:
            new_crypto.save_crypto()
        except Exception as error:
            print(str(error))
            return {"message": "An error ocurred trying to create crypto."}, 500 #Internal Server Error
        
        return new_crypto.json(), 201
