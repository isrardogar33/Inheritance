class Animal:
    def __init__(self):
        self.animal_attr = "I am an animal."
        
    def animal_method(self):
        print("Calling animal method.")
        
class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.cat_attr = "I am a cat."
        
    def cat_method(self):
        print("Calling cat method.")
        
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.dog_attr = "I am a dog."
        
    def dog_method(self):
        print("Calling dog method.")
        
c = Cat()
c.cat_method()
c.animal_method()
print(c.cat_attr)
print(c.animal_attr)

d = Dog()
d.dog_method()
d.animal_method()
print(d.dog_attr)
print(d.animal_attr)