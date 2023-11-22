class Parent1:
    def method1(self):
        print("Calling method1 from Parent1")

class Parent2:
    def method2(self):
        print("Calling method2 from Parent2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Calling method3 from Child")

c = Child()
c.method1()
c.method2()
c.method3()