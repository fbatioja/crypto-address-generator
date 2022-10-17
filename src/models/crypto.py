from sql_alchemy import database

class CryptoModel(database.Model):
    __tablename__ = "cryptos"

    crypto_id = database.Column(database.Integer, primary_key=True)
    crypto = database.Column(database.String(3))

    def __init__(self, crypto):
        self.crypto = crypto

    def json(self):
        return {
            "crypto_id": self.crypto_id,
            "crypto": self.crypto,
        }
    
    @classmethod
    def find_crypto_by_id(cls, crypto_id):
        crypto = cls.query.filter_by(crypto_id=crypto_id).first()

        if not crypto:
            return None

        return crypto
    
    @classmethod
    def find_crypto(cls, crypto):
        _crypto = cls.query.filter_by(crypto=crypto).first()

        if not _crypto:
            return None

        return _crypto
    
    def save_crypto(self):
        database.session.add(self)
        database.session.commit()
