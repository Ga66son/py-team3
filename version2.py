import random
from abc import ABC, abstractmethod


# --- Mixin for generating random codes ---
class RandomCodeMixin:
    def generate_code(self):
        return random.randint(1000, 9999)


# --- Abstract Class ---
class Technique(ABC):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def category(self):
        pass


# --- Inheritance ---
class Computer(Technique):
    def __init__(self, name, price, stock, specs):
        super().__init__(name, price, stock)
        self.specs = specs

    def category(self):
        return "Computer"

    def __str__(self):
        return f"{self.name} ({self.category()}): ${self.price}, Stock: {self.stock}"


class HomeTechnique(Technique):
    def __init__(self, name, price, stock, power):
        super().__init__(name, price, stock)
        self.power = power

    def category(self):
        return "Home Appliance"

    def __str__(self):
        return f"{self.name} ({self.category()}): ${self.price}, Stock: {self.stock}"


# --- User Class ---
class User(RandomCodeMixin):
    def __init__(self, name, email, password, is_vip=False):
        self.name = name
        self.email = email
        self.password = password
        self.is_vip = is_vip
        self.user_code = self.generate_code()

    def __str__(self):
        return f"User: {self.name}, VIP: {self.is_vip}, Code: {self.user_code}"


# --- Shopping Cart ---
class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}")
        self.items.append((product, quantity))

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total * 0.9 if self.user.is_vip else total

    def __str__(self):
        cart_details = "\n".join(
            [f"{product.name} x {quantity}" for product, quantity in self.items]
        )
        return f"Cart for {self.user.name}:\n{cart_details}\nTotal: ${self.calculate_total():.2f}"

# --- Order ---
class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.order_code = self.generate_order_code()

    def generate_order_code(self):
        return f"ORD-{random.randint(1000, 9999)}"

    def validate_order(self):
        if not self.cart.items:
            raise ValueError("The cart is empty!")
        for product, quantity in self.cart.items:
            if product.stock < quantity:
                raise ValueError(f"Insufficient stock for {product.name}!")

    def process_order(self):
        self.validate_order()
        for product, quantity in self.cart.items:
            product.stock -= quantity
        return f"Order {self.order_code} successfully processed for {self.user.name}!"

    def __str__(self):
        return f"Order Code: {self.order_code}\nUser: {self.user.name}\nTotal: ${self.cart.calculate_total():.2f}"

def validate_user_data(email, password):
    if "@" not in email:
        raise ValueError("Invalid email format")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

from models import User, Computer, HomeTechnique, Cart, Order

# --- Create User ---
user = User(name="lizi salt", email="lizi@example.com", password="securepass", is_vip=True)
print(user)

# --- Create Products ---
laptop = Computer(name="Gaming Laptop", price=1200, stock=5, specs="16GB RAM, i7 CPU")
fridge = HomeTechnique(name="Refrigerator", price=800, stock=2, power="300W")
print(laptop)
print(fridge)

# --- Add Products to Cart ---
cart = Cart(user)
cart.add_to_cart(laptop, 1)
cart.add_to_cart(fridge, 1)
print(cart)

# --- Create and Process Order ---
order = Order(user, cart)
print(order.process_order())
print(order)
