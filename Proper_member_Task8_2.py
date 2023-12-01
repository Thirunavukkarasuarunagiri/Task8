#2 Create proper member variables inside the task if required and use them when necessary.For example for this task. create a class private variable named pi=3.141

class myClass:
    a = 33
    def __privMeth(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private Variable value:", myClass.a)

foo = myClass()
foo.hello()
print("Class Attribute value:", myClass.a)