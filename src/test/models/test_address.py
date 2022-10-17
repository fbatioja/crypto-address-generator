from models.address import AddressModel


def test_new_address():
    _address = AddressModel('BTC', 'ABC123')
    
    assert _address.address == 'ABC123'
    assert _address.crypto == 'BTC'