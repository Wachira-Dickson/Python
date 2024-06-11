class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.bark()
