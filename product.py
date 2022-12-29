from json import JSONEncoder, JSONDecoder, JSONDecodeError, loads

class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__

class Decoder(JSONDecoder):

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        prod = Product(*vals)
        return prod


class Product:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other) -> bool:
        if type(other) == type(self):
            return self.name == other.name
        else:
            return False

    def __hash__(self):
        return hash(self.name)