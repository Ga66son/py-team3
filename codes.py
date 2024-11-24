# OOP გვეხმარება რომ შევქმნათ კოდი და გამოვიყენოთ მრავალჯერ
# კლასი წარმოადგენს შაბლონს, რომელიც აღწერს რა მონაცემები და ლოგიკა ექნება მისი საშუალებით შექმნილ ობიექტს
# class Car:
    #def __new__(cls):
        #creates an actual object
    #def __init__(self):
        #set initial values
    #class attributes
    #car_types = ["sedan", "minivan"]
    #instance method
    #def start(self):
        #if self.is_running:
            #print("car is already running")
#car = Car()

# class Car:
#     wheel_amount = 4
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
    
#     @classmethod
#     def get_wheel_amount(cls):
#         return cls.wheel_amount



# car = Car("red",180)

# print(car.get_wheel_amount())

# class Planet:
#     type = "round"
#     turn = "around the Sun"
#     size = "Big"

#     def __init__(self, has_water, atmosphere, has_life):
#         self.has_water = has_water
#         self.atmosphere = atmosphere
#         self.has_life = has_life

# earth = Planet(True, "Oxigen", True)

# print(earth.has_life)

# print(earth.type)

# print(earth.turn)


# class Student:
#     university = "Skillwill"
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

#     def is_passing(self):
#         if self.grade > 60:
#             return True
#         else:
#             return False
    
#     def increase_grade(self, n):
#         self.grade += n

# student1 = Student("Giorgi", 75, 33)

# student1.increase_grade(10)

# print(student1.grade)

# class Person:
#     """Parent class"""

# class Student(Person):
#     """Child class"""


# მემკვიდრეობის ტიპები

#     Single - შვილობილი კლასი მხოლოდ ერთ კლასს აექსთენდებს
#     Multiple - შვილობილი კლასი ერთდროულად რამდენიმე კლასს აექსთენდებს
#     Multilevel - შვილობილი აექსთენდებს მშობელს, მშობელი წარმოადგენს სხვა კლასის შვილს
# #     Hierarchical - მშობელ კლასს აექსთენდებს რამდენიმე შვილობილი კლასი
# #     Hybrid - რამდენიმე ტიპის მემკვიდრეობაა გაერთიანებული

# # MRO - იერარქია, რომელიც მიგვითითებს რა თანმიმდევრობით მოიძებნება ატრიბუტები და მეთოდები მათზე წვდომისას 

# class CreateMixin:
#     def attributes(self):
#         return f"name: {self.name}, surname: {self.surname}, age: {self.age}"

# class Person(CreateMixin):
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
    

# class Student(Person):
#     def __init__(self, name, surname, age, university):
#         super().__init__(name, surname, age)
#         self.university = university

#     def display(self):
#         self.log(f"name: {self.name}")
#         return f"Product: {self.product_name}"


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed, current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        return "car stopped"

class SportCar(Car):
    def __init__(self, max_speed, current_speed):
        super().__init__(max_speed, current_speed)
    def start_engine(self):
        result = super().start_engine()
        print(result)
        print(f"Max speed: {self.max_speed}")
        
    def stop_engine(self):
        result = super().stop_engine()
        print(result)
        self.current_speed = 0
        print(f"Current speed after stopping: {self.current_speed}")






    




