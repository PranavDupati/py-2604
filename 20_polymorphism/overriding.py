# Method Overriding 

class Animal:
    
    def sound(self):
        print("Animal Makes Some Sound")
        
class Dog(Animal):
    
    def sound(self):
        print("Dog Makes Woff Sound")
        
class Cat(Animal):
    
    def sound(self):
        print("Cat Makes Meow Sound")
        
animal = Animal()
animal.sound()

cat = Cat()
cat.sound()

dog = Dog()
dog.sound()