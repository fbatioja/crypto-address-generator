# crypto-address-generator

## How to run

### Create virtual environment.

```
python3 -m venv venv
```

### Install packages

```
source venv/bin/active
pip install -r requirements.txt
```

### Run API

```
source venv/bin/active
python src/app.py
```

## SonarCloud and CI

SonarCloud was used as a code quality control tool. It generates a report on the code quality.

Project url: https://sonarcloud.io/project/overview?id=lucas54neves_crypto-address-generator

## Endpoints

### /\<string:crypto>/addresses

#### Method GET

Return all address from a crypto.

##### Example

URL: http://127.0.0.1:5000/btc/addresses

Response:

```
{
    "addresses": [
        {
            "address_id": 1,
            "crypto": "BTC",
            "address": "e9bae7af89c6a7f73f4681ee054817c2f2871725"
        },
        {
            "address_id": 2,
            "crypto": "BTC",
            "address": "76dc1f28806ef8bac63d90fc0fddbcdaa6fa6512"
        },
        {
            "address_id": 4,
            "crypto": "BTC",
            "address": "1NjuKoant7tQ4maQUGTLjwmdVgaJjbL521"
        },
        {
            "address_id": 5,
            "crypto": "BTC",
            "address": "1NjuKoant7tQ4maQUGTLjwmdVgaJjbL521"
        },
        {
            "address_id": 6,
            "crypto": "BTC",
            "address": "1NjuKoant7tQ4maQUGTLjwmdVgaJjbL521"
        },
        {
            "address_id": 7,
            "crypto": "BTC",
            "address": "1NjuKoant7tQ4maQUGTLjwmdVgaJjbL521"
        }
    ]
}
```

#### Method POST

Generate a address.

##### Example

URL:

Request body:

```
{
    "private_key": "33353816f44447ede1a74fc278b9b4bda415218b86ffe8166b0cba65c1ee5510"
}
```

Response:

```
{
    "address_id": 13,
    "crypto": "ETC",
    "address": "0xEDb515cf8a1A3E04db9fC08058770091fd4C13B7"
}
```

### /\<string:crypto>/address/<string:address_id>

#### Method GET

Return a address by address id

#### Example

URL: http://127.0.0.1:5000/btc/address/1

Response:

```
{
    "address_id": 1,
    "crypto": "BTC",
    "address": "e9bae7af89c6a7f73f4681ee054817c2f2871725"
}
```
