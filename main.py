#Person
class Person:
    def __init__(self,name,family):
        self.name = name
        self.family = family
        
    def full_name(self):
        return f"{self.name} {self.family}"
    
    
#Employee
class Employee(Person):
    salery = 3000
    def __init__(self,name,family,position):
        super().__init__(name, family)
        self.position = position
    
    def job(self):
        return f"I am an employee, my name is {self.full_name()} and I work as a {self.position}."
    

#Manager
class Manager:
    def authority(self):
        return "I am a manager and I have authority to approve or reject projects."
    
#CTO    
class CTO(Employee,Manager):
    salery  = 6000
    def job(self):
        return f"I am an employee, my name is {self.full_name()} and I work as a CTO."
        
#Intern
class Intern(Employee):
    salery = 1000
    def job(self):
        return "learning new things"

print('********************************')

emp1 = Employee('amirreza','attary','Backend Developer')
print(emp1.job())
print(emp1.salery)

print('********************************')

emp2 = CTO('amirreza','attary','Backend Developer')
print(emp2.job())
print(emp2.salery)
print(emp2.authority())

print('********************************')

emp3 = Intern('amirreza','attary','Backend Developer')
print(emp3.job())
print(emp3.salery)


