from json import JSONEncoder, JSONDecoder, JSONDecodeError, loads

from product import Product


class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__

class Decoder(JSONDecoder):

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        ord = Order(*vals)
        return ord


class Order:
    def __init__(self, order_number, order_product, order_quantity, order_address):
        self.order_number = order_number
        self.order_product=order_product
        self.order_quantity=order_quantity
        self.order_address=order_address

    def __eq__(self, other) -> bool:
        if type(other) == type(self):
            return self.order_number,self.order_product,self.order_quantity,self.order_address
        else:
            return False

    def __hash__(self):
        return hash(self.order_number,self.order_product,self.order_quantity,self.order_address)

    def __str__(self):
        return f'{self.order_number} {self.order_product} {self.order_quantity} {self.order_address}'