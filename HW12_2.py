class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return self.name

class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return self.first_name + " " + self.last_name

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = quantity

    def get_total_price(self):
        total = 0
        for product in self.products:
            total = total + product.price * self.products[product]
        return total

    def __str__(self):
        result = ""
        result = result + "Покупець: " + str(self.customer) + "\n"
        result = result + "Товари:\n"

        for product in self.products:
            result = result + product.name + ": " + str(self.products[product]) + " шт.\n"

        result = result + "Сума: " + str(self.get_total_price())
        return result
