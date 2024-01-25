class Database:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price):
        self.products[product_id] = {'name': name, 'price': price}

    def get_product_info(self, product_id):
        return self.products.get(product_id)

class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity

    def remove_from_cart(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] -= quantity
            if self.items[product_id] <= 0:
                del self.items[product_id]

    def view_cart(self):
        return self.items

class WebFront:
    def __init__(self, database, cart):
        self.database = database
        self.cart = cart

    def display_products(self):
        return self.database.products

    def add_to_cart(self, product_id, quantity):
        product_info = self.database.get_product_info(product_id)
        if product_info:
            self.cart.add_to_cart(product_id, quantity)
            return f"Added {quantity} {product_info['name']} to the cart."
        else:
            return "Product not found."

    def remove_from_cart(self, product_id, quantity):
        product_info = self.database.get_product_info(product_id)
        if product_info:
            self.cart.remove_from_cart(product_id, quantity)
            return f"Removed {quantity} {product_info['name']} from the cart."
        else:
            return "Product not found."

    def view_cart(self):
        return self.cart.view_cart()


# Example usage:
# Create instances of Database, Cart, and WebFront
database = Database()
cart = Cart()
webfront = WebFront(database, cart)

# Add some products to the database
database.add_product(1, 'Laptop', 999.99)
database.add_product(2, 'Smartphone', 499.99)

# Display available products
print("Available Products:")
print(webfront.display_products())

# Add products to the cart
webfront.add_to_cart(1, 2)
webfront.add_to_cart(2, 1)

# View the cart
print("Shopping Cart:")
print(webfront.view_cart())

# Remove products from the cart
webfront.remove_from_cart(1, 1)

# View the updated cart
print("Updated Cart:")
print(webfront.view_cart())
