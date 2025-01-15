from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,family):
        self.name = name
        self.family = family
    
    @abstractmethod
    def full_name(self):
        pass


class Employee(Person):
    salery = 3000
    

    def full_name(self):
        return f"{self.name} {self.family}"
    

class Employer(Person):
    salery = 100000
    
    def full_name(self):
        return f"{self.name} {self.family}"
        
        
emp_1 = Employee('amir','attary')
print(emp_1.full_name())

emp_2 = Employer('maryam','farjan')
print(emp_2.full_name())

