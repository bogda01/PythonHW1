from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import category


class Encoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Categories:
    categories = []

    @classmethod
    def load_categories(cls):
        decoder = category.Decoder()

        try:
            with open("categories.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_category = decoder.decode(data)
                    if decoded_category not in cls.categories:
                        cls.categories.append(decoded_category)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.categories = []
        return cls.categories

    @classmethod
    def remove_category(cls, category):
        cls.load_categories()
        if category in cls.categories:
            cls.categories.remove(category)
            with open("categories.txt", 'w') as f:
                for category in cls.categories:
                    e = Encoder()
                    encoded_category = e.encode(category)
                    dump(encoded_category, f)
                    f.write("\n")

    @classmethod
    def add_category(cls, category):
        cls.load_categories()
        if category not in cls.categories:
            with open("categories.txt", 'a') as f:
                e = Encoder()
                encoded_category = e.encode(category)
                dump(encoded_category, f)
                f.write("\n")
