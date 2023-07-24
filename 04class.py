class Point: 
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
    def draw(self):
        print("draw")

# point1 = Point()
# point1.x = 10
# point1.y = 20
# point1.draw()
# print(point1.x)

# point2 = Point()
# print(point1)

#? declare value using contructor
# point = Point(10, 20)
# print(point.x)

#! exercise
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"{self.name} is talking")
        
# person1 = Person("Joy")
# person1.talk()

#? inheritance
class Animal:
    def __init__(self, spiece):
        self.spiece = spiece
    def walk(self):
        print("walk")
        
        
class Dog(Animal):
    pass
    
    
        
class Cat(Animal):
    def meow(self):
        print("meow")

dog = Dog("dog")
dog.walk()
print(dog.spiece)

boba = Cat("cat")
boba.walk()
boba.meow()