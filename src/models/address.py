from sql_alchemy import database

class AddressModel(database.Model):
    __tablename__ = "addresses"

    address_id = database.Column(database.Integer, primary_key=True)
    crypto = database.Column(database.String(3))
    address = database.Column(database.String(40))

    def __init__(self, crypto, address):
        self.crypto = crypto
        self.address = address

    def json(self):
        return {
            "address_id": self.address_id,
            "crypto": self.crypto,
            "address": self.address,
        }
    
    @classmethod
    def find_address(cls, address_id, crypto):
        address = cls.query.filter_by(address_id=address_id, crypto=crypto).first()

        if not address:
            return None

        return address
    
    @classmethod
    def find_address_by_crypto(cls, crypto):
        addresses = cls.query.filter_by(crypto=crypto)

        if not addresses:
            return None

        return addresses
    
    def save_address(self):
        database.session.add(self)
        database.session.commit()
