from models.address import AddressModel


def test_new_address():
    _address = AddressModel('BTC', 'ABC123')
    
    assert _address.address == 'ABC123'
    assert _address.crypto == 'BTC'

    address_json = _address.json()

    assert address_json['address'] == 'ABC123'
    assert address_json['crypto'] == 'BTC'