import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.quantity} units"

product1 = Product("Laptop", 1200, 5)
product2 = Product("Phone", 800, 10)
product3 = Product("Tablet", 300, 15)

products = [product1, product2, product3]

def serialize_products(products, filename="products.json"):
    def product_serializer(obj):
        if isinstance(obj, Product):
            return {"name": obj.name, "price": obj.price, "quantity": obj.quantity}
        raise TypeError("Cannot serialize object")

    with open(filename, 'w') as json_file:
        json.dump(products, json_file, default=product_serializer, indent=4)

serialize_products(products)

def deserialize_products(filename="products.json"):
    def product_deserializer(json_data):
        return Product(json_data['name'], json_data['price'], json_data['quantity'])

    with open(filename, 'r') as json_file:
        return json.load(json_file, object_hook=product_deserializer)

loaded_products = deserialize_products()

for product in loaded_products:
    print(product)