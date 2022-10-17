import hashlib
import time


def generate_address(crypto):
    time_now = time.time() * 1000

    str2hash = f'{time_now}{crypto}'
    
    result = hashlib.sha1(str2hash.encode())

    return result.hexdigest()