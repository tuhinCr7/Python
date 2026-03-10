class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} removed from cart")
                return
        print("Product not found")

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        print("\nCart Items:")
        for product in self.products:
            print(product.name, "-", product.price)

p1 = Product("Laptop", 80000)
p2 = Product("Mouse", 500)
p3 = Product("Keyboard", 1500)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.show_cart()

print("\nTotal Price:", cart.calculate_total())

cart.remove_product("Mouse")

cart.show_cart()
print("\nTotal Price:", cart.calculate_total())