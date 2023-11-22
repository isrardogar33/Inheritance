class Grandparent:
    def __init__(self):
        self.grandparent_attr = "I am the grandparent."
        
    def grandparent_method(self):
        print("Calling grandparent method.")
        
class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        self.parent_attr = "I am the parent."
        
    def parent_method(self):
        print("Calling parent method.")
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "I am the child."
        
    def child_method(self):
        print("Calling child method.")
        
c = Child()
c.child_method()
c.parent_method()
c.grandparent_method()
print(c.child_attr)
print(c.parent_attr)
print(c.grandparent_attr)