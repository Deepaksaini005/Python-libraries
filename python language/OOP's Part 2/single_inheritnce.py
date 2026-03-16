# Parent class
class Animal:
    def speak(self):
        print("Animal can speak")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object of Dog
d = Dog()

d.speak()
d.bark()
