from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import product

class Encoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Products:

    products = []

    @classmethod
    def load_products(cls):
        decoder = product.Decoder()

        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data)
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.products = []
        return cls.products

    @classmethod
    def remove_product(cls, prod):
        cls.load_products()
        if prod in cls.products:
            cls.products.remove(prod)
            with open("products.txt", 'w') as f:
                for prod in cls.products:
                    e = Encoder()
                    encoded_prod = e.encode(prod)
                    dump(encoded_prod, f)
                    f.write("\n")

    @classmethod
    def add_product(cls, prod):
        cls.load_products()
        if prod not in cls.products:
            with open("products.txt", 'a') as f:
                e = Encoder()
                encoded_prod = e.encode(prod)
                dump(encoded_prod, f)
                f.write("\n")
