import random
from abc import ABC, abstractmethod

class CodeMixin:
    def generate_random_code(self):
        return random.randint(1000, 9999)

class Technique(ABC):
    def __init__(self, id, brand, price, balance):
        self.id = id
        self.brand = brand
        self.price = price
        self.balance = balance

    def buy(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Can't buy negative number of items.")
            self.balance += amount
            print(f"{amount} items of {self.brand} were bought. Stock balance: {self.balance}")
        except ValueError as e:
            print(f"Purchase error: {e}")

    def sell(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Can't sell negative number of items.")
            if self.balance < amount:
                raise ValueError("Not enough items in the stock balance.")
            self.balance -= amount
            print(f"{amount} items of {self.brand} were sold. Stock balance: {self.balance}")
        except ValueError as e:
            print(f"Sale error: {e}")

    def check_balance(self):
        return self.balance


class Computer(Technique, CodeMixin):
    def __init__(self, id, brand, price, balance, processor, os, disk):
        super().__init__(id, brand, price, balance)
        self.processor = processor
        self.os = os
        self.disk = disk
       

class HomeTecnique(Technique, ABC):
    def __init__(self, id, brand, price, balance, warranty):
        super().__init__(id, brand, price, balance)
        self.warranty = warranty
    
    @abstractmethod
    def warranty_info(self):
        pass


class WashingMachine(HomeTecnique):
    def __init__(self, id, brand, price, balance, warranty, kg, dryer):
        super().__init__(id, brand, price, balance, warranty)
        self.kg = kg
        self.dryer = dryer

    def start_machine(self):
        print(f"Washing machine {self.brand} is ON.")

    def stop_machine(self):
        print(f"Washing machine {self.brand} is OFF.")

    def warranty_info(self):
        return f"Washing machine has warranty of {self.warranty} years. In case of problem please contact the {self.brand} service center"


class Fridge(HomeTecnique):
    def __init__(self, id, brand, price, balance, warranty, min_temperature, volume, eco):
        super().__init__(id, brand, price, balance, warranty)
        self.min_temperature = min_temperature
        self.volume = volume
        self.eco = eco

    def super_freeze_on(self):
        print("Super Freeze mode is ON.")

    def super_freeze_off(self):
        print("Super Freeze mode is OFF.")

    def warranty_info(self):
        return f"Fridge has warranty of {self.warranty} years. In case of problem please contact the {self.brand} service center"


# მაცივრის ობიექტის შექმნა

fridge = Fridge(1, "LG", 2500, 10, 5, -20, 110, True)

fridge.super_freeze_on()

fridge.buy(2)

fridge.sell(1)

fridge.check_balance()


# კომპიუტერის ობიექტის შექმნა
computer = Computer(1, "Acer", 1500, 5, "Intel i7", "Windows 11", "512GB SSD")

# შემთხვევითი კოდის გენერაცია
random_code = computer.generate_random_code()
print(f"Random code for the computer: {random_code}")


