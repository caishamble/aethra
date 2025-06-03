"""
3 - 70 pts (Classes)

Pt. 1 - Product class
Create a class called Product with the following attributes:
    - id (int)
    - name (str)
    - price (float)

__init__ method should initialize the attributes, assume types are correct.
    Default values are 0 for id, "Hanissa" for name, and 0.0 for price.

__str__ method should return a string in the following format:
    "ID: {}, Name: {}, Price: {}"

__repr__ method should return a string in the same format as __str__.

__eq__ method should return True if the id's are the same, False otherwise.

Pt. 2 - Inventory class
Create a class called Inventory with the following attributes:
    - products (list of Product objects)

__init__ method should initialize the products attribute as default value of empty list -> [].
    check if each product in products is a Product object, if not, set it to default Product object.
    then, add the product to the products list.

__str__ method should return a string in the following format:
    "Inventory of products: {}" where each product, if there is more than 1, is separated by a SEMICOLON
    and a SPACE. Ex: "Inventory of products: (ID: 1, Name: Hanissa, Price: 0.0); (ID: 2, Name: Hanissa, Price: 0.0)"

add_product method should add a product to the products list, only if the product is not already in the list.
    If the product is already in the list, simply don't add it again

__add__ method should check for two types of inputs (assume incoming type will be one of the two):
    - if the input is a Product object, add it to the products list (follow logic of add_product method)
    - if the input is an Inventory object, add all the product prices together and return the sum.
"""

"""
Test Cases
p1 = Product(1, "Hanissa", 25.0)
p2 = Product(2, "John", 3.2)
p3 = Product(3, "Doe", 4.5)
print(p1)   # ID: 1, Name: Hanissa, Price: 25.0
print(p2)   # ID: 2, Name: John, Price: 3.2
print(p3)   # ID: 3, Name: Doe, Price: 4.5
print(p1 == p2) # False
print(p1 == p1) # True

i1 = Inventory([p1, p2])
print(i1)   # Inventory of products: (ID: 1, Name: Hanissa, Price: 25.0); (ID: 2, Name: John, Price: 3.2)
i1.add_product(p3)
print(i1)   # Inventory of products: (ID: 1, Name: Hanissa, Price: 25.0); (ID: 2, Name: John, Price: 3.2); (ID: 3, Name: Doe, Price: 4.5)
i1.add_product(p1)
print(i1)   # Inventory of products: (ID: 1, Name: Hanissa, Price: 25.0); (ID: 2, Name: John, Price: 3.2); (ID: 3, Name: Doe, Price: 4.5)
i2 = Inventory([p1, p2, p3])
print(i2)   # Inventory of products: (ID: 1, Name: Hanissa, Price: 25.0); (ID: 2, Name: John, Price: 3.2); (ID: 3, Name: Doe, Price: 4.5)
print(i1 + i2)  # 65.4
print(i1 + p3)  # None
print(i1)   # Inventory of products: (ID: 1, Name: Hanissa, Price: 25.0); (ID: 2, Name: John, Price: 3.2); (ID: 3, Name: Doe, Price: 4.5)
"""

class Product:
    def __init__(self, id = 0, name = "Hanissa", price = 0.0):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}"
        #return "ID: {}, Name: {}, Price: {}".format(self.id, self.name, self.price)

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}"
        #return "ID: {}, Name: {}, Price: {}".format(self.id, self.name, self.price)

    def __eq__(self, other):
        return self.id == other.id