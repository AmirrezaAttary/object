class Employee:
    salery = 3000
    total_employee = 0
    
    def __init__(self,name,family):
        self.name = name
        self.family = family
        
    
    @property
    def full_name(self):
        return f"{self.name} {self.family}"
    
    @full_name.setter
    def full_name(self,name_family):
        self.name, self.family = name_family.split(" ")
    
    @full_name.deleter
    def full_name(self):
        self.name = None
        self.family = None
        
emp_1 = Employee('amir','attary')

print(emp_1.full_name)

emp_1.full_name = "hasan ajamy"

print(emp_1.full_name)

del emp_1.full_name

print(emp_1.full_name)
