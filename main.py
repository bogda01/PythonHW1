from category import Category
from categories import Categories
from products import Products
from product import Product
from order import Order
from orders import Orders

from json import JSONDecoder, JSONEncoder, JSONDecodeError
if __name__ == "__main__":
    cat_1 = Category("Amplifiers")
    cat_2 = Category("Receivers")
    cat_3 = Category("Speakers")

    Categories.add_category(cat_1)
    Categories.add_category(cat_2)
    Categories.add_category(cat_3)

    def fun_category():
        print("1. Add a category")
        print("2. Remove a category")
        print("3. Display all the categories")

        option = int(input("Enter your option here: "))
        if option == 1:
            option_add_category = str(input("Enter category name you want to add: "))
            cat_add = Category(option_add_category)
            Categories.add_category(cat_add)
            print("Category inserted successfully...")
        if option == 2:
            option_del_category = str(input("Enter category name you want to delete: "))
            cat_del = Category(option_del_category)
            cat_del = Categories.remove_category(cat_del)
            print("Category deleted successfully...")
        if option == 3:
            try:
                categories = Categories.load_categories()
                for cat in categories:
                    print(cat.name)
            except JSONDecodeError as e:
                categories = None

    # Submenus
    def fun_product():
        print("1. Add a product")
        print("2. Remove a product")
        print("3. Display all the products")

        option = int(input("Enter your option here: "))
        if option == 1:
            option_add_product = str(input("Enter product name you want to add: "))
            prod_add = Product(option_add_product)
            Products.add_product(prod_add)
            print("Product added successfully...")
        if option == 2:
            option_del_product = str(input("Enter product name you want to delete: "))
            prod_del = Product(option_del_product)
            Products.remove_product(prod_del)
            print("Product deleted successfully...")
        if option == 3:
            try:
                products = Products.load_products()
                for prod in products:
                    print(prod.name)
            except JSONDecodeError as e:
                products = None

    def fun_order():
        print("1. Place an order")
        print("2. Remove an order")
        print("3. Display all the orders")

        option = int(input("Enter your option here: "))
        if option == 1:
            order_number = int(input("Enter the number of the order: "))
            order_product = str(input("Enter the product you want to order: "))
            order_quantity = int(input("Enter the quantity of the product: "))
            order_address = str(input("Enter the address where you want the order to be delivered: "))
            ord_add = Order(order_number,order_product,order_quantity,order_address)
            Orders.add_order(ord_add)
            print("Order placed successfully...")
        if option == 2:
            option_del_order = int(input("Enter order number you want to delete: "))
            if Orders.find_order(option_del_order):
                Orders.remove_order(option_del_order)
                print("Order deleted successfully...")
            else:
                print("Couldnt delete")
        if option == 3:
            try:
                orders = Orders.load_orders()
                for ord in orders:
                    print(ord)
            except JSONDecodeError as e:
                orders = None

    def fun_four():
        print("Exit")

    def error_handler():
        print("Action not supported")

    # Menu
    print("1. Categories")
    print("2. Products")
    print("3. Orders")
    print("4. Exit")

    option = int(input("Enter an option: "))

    actions = {1 : fun_category, 2 : fun_product, 3 : fun_order, 4 : fun_four}

    action = actions.get(option, error_handler)
    action()