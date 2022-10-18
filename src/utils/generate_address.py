from bitcoin import *
from eth_account import Account


def generate_address(crypto, private_key):
    if crypto == 'BTC':
        public_key = privtopub(private_key)

        return pubtoaddr(public_key)

    if crypto == 'ETC':
        _private_key = "0x" + private_key
        _account = Account.from_key(_private_key)
        
        return _account.address

    return None

    # time_now = time.time() * 1000

    # str2hash = f'{time_now}{crypto}'
    
    # result = hashlib.sha1(str2hash.encode())

    # return result.hexdigest()