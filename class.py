# class factory:
#     a = 12     # attribute

#     def hello(self):              # method.
#         print("hello inside")

# factory()
# print(factory().a)
# factory().hello()
# obj = factory()      # object creation.
# print(obj.a)
# obj.hello()


# class car:
#     model = "german"     # class attribute.
# # this __init__ is a constructor.
#     def __init__(self, model, brand):
#         self.model = model          # instance attribute.
#         self.brand = brand          # instance attribute.

#     def show(self):
#         print(f"car model is {self.model} and brand is {self.brand}")


# x = car("american", "mustang")
# y = car("german", "bmw")
# x.show()
# y.show()

# # inheritance.
# class animal:                        # super/parent class.
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print("animal eat.")

#     def sleep(self):
#         print("animal sleep.")

#     def showname(self):
#         print(f"dog name is {self.name}")

# class dog(animal):                   # sub/child class.
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f" {self.name} eats and sleeps.")

#     def showage(self):
#         print(f"{self.name} is {self.age} years old.")

# x = dog("starky", 20)
# x.sleep()
# x.eat()
# x.show()
# x.showname()
# x.showage()

# 1. inheritance.

# class factory:
#     def __init__(self, material, zip):
#         self.material = material
#         self.zip = zip

# class bhopalFactory(factory):
#     def __init__(self, material, zip, color):
#         super().__init__(material, zip)
#         self.color = color

# class puneFactory(bhopalFactory):
#     def __init__(self, material, zip, color, pocket):
#         super().__init__(material, zip, color)
#         self.pocket = pocket

#     def show(self):
#         print(
#             f"this is a {self.color} color {self.material} cloth with {self.zip} zips and {self.pocket} pockets.")

# obj = puneFactory("cotton", 4, "black", 2)
# obj.show()

# 2. polymorphism.
# pyhton doesnot support method overloading because the latest definition will overwrite the previous one.
# poymorphism is acheived by method overriding and duck typing.
# this is method overriding. and it works with inheritance.

# class animal:
#     def show(self):
#         print("i am animal.")

# class human(animal):
#     def show(self):
#         print("i am human.")

# x = human()
# x.show()

# duck typing.
# class duck:
#     def talk(self):
#         print("duck quack.")

# class human:
#     def talk(self):
#         print("human talk.")

# x = duck()
# y = human()
# x.talk()
# y.talk()


# 3. encapsulation. "__" means private and '_' means protected.
# mostly private is used for access control of variables or methods.

# class factory:
#     __a = "pune"

#     def show(self):
#         print(factory.__a)

# obj = factory()
# obj.show()


# 4. abstraction. it doesnt exist in python . it is acheived using library.

# from abc import ABC, abstractmethod
# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
#     @abstractmethod
#     def area(self):
#         pass

# class square(abstract):
#     def __init__(self,side):
#         self.side = side
#     def perimeter(self):
#         print("this is perimeter of square.")
#     def area(self):
#         print("this is area of square.")

# class circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
#     def perimeter(self):
#         print("this is perimeter of circle.")
#     def area(self):
#         print("this is area of circle.")

# x = circle(7)
# y = square(10)
# x.area()
# y.perimeter()

