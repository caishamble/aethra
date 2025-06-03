class Product:
    def __init__(self, id = 0, name = "Hanissa", price = 0.0):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return "ID: {}, Name: {}, Price: {}".format(self.id, self.name, self.price)

    def __repr__(self):
        return "ID: {}, Name: {}, Price: {}".format(self.id, self.name, self.price)

    def __eq__(self, other):
        return self.id == other.id

class Inventory:
    def __init__(self, products=[]):
        self.products = []
        for every_product in products:
            if not isinstance(every_product, Product):
                every_product = Product()
            self.products.append(every_product)

    def __str__(self):
        cnt = 1
        new_str = "Inventory of products: "
        for every_product in self.products:
            if cnt < len(self.products):
                new_str += '(' + str(every_product) + ')' + '; '
            elif cnt == len(self.products):
                new_str += '(' + str(every_product) + ')'
            cnt += 1
        return new_str

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def __add__(self, other):
        if isinstance(other, Product):
            self.add_product(other)
        elif isinstance(other, Inventory):
            return sum([product.price for product in self.products]) + sum([product.price for product in other.products])



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
print(i1 + i2)  # explain this 32.7: (i1) -> 25.0 + 3.2 + 4.5 = 32.7, (i2) -> 25.0 + 3.2 + 4.5 = 32.7, 32.7 + 32.7 = 65.4
print(i1 + p3)  # None
print(i1)   # Inventory of products: (ID: 1, Name: Hanissa, Price: 25.0); (ID: 2, Name: John, Price: 3.2); (ID: 3, Name: Doe, Price: 4.5)