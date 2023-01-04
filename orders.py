from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump

import order


class Encoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Orders:
    orders = []

    @classmethod
    def load_orders(cls):
        decoder = order.Decoder()

        try:
            with open("orders.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_order = decoder.decode(data)
                    if decoded_order.order_number not in cls.orders:
                        cls.orders.append(decoded_order)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.orders = []
        return cls.orders

    @classmethod
    def remove_order(cls, ord_number):
        cls.orders.pop(ord_number - 1)
        with open("orders.txt", 'w') as f:
            for order in cls.orders:
                e = Encoder()
                encoded_order = e.encode(order)
                dump(encoded_order, f)
                f.write("\n")

    @classmethod
    def add_order(cls, order):
        cls.load_orders()
        if order.order_number not in cls.orders:
            with open("orders.txt", 'a') as f:
                e = Encoder()
                encoded_order = e.encode(order)
                dump(encoded_order, f)
                f.write("\n")

    @classmethod
    def find_order(cls, ord_number):
        cls.load_orders()
        ok = 0
        for i in cls.orders:
            if i.order_number == ord_number:
                return True
        if ok == 0:
            print("Couldn't find anything")
            return False
