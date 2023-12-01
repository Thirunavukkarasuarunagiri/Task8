# 1 Create a program class called circle with constructor which will take a list as an argument for the task.The List is[10,501,22,37,100,999,87,351]
class Circle:
    def __init__(self):
        # initializing instance variable
        self.num = [10, 501, 22, 37, 100, 999, 87, 351]
    def read_number(self):
        print(self.num)


obj = Circle()

obj.read_number()