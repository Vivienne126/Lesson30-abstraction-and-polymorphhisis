from abc import ABC, abstractmethod
class main_class(ABC):
    def print(self,x):
        print("The value is " , x)
    @abstractmethod
    def task(self):
        print("This is abstract method")
class sub_class(main_class):
    def task(self):
        print("This abstract method of task class")
obj=sub_class()
obj.task()
obj.print(100)