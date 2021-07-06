from typing import Optional


class Product(object):
    name: str
    price: Optional[str]

    def __init__(self, name: Optional[str] = None, price: Optional[str] = None):
        self.name = name
        self.price = price
