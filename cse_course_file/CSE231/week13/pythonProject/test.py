class A:
    x = 10

    def __init__(self, a):
        self.x = a
    def __str__(self):
        return f"{x},{self.x}"

a_instance = A(20)
print(a_instance) # Output: 10,20