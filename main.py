import datetime

class Employee:
    salery = 3000
    total_employee = 0
    
    def __init__(self,name,family):
        self.name = name
        self.family = family
        Employee.total_employee += 1
    
    def full_name(self):
        return f"{self.name} {self.family}"
    
    @classmethod
    def raise_salery(cls,new_salery):
        if type(new_salery) == int:
            cls.salery = new_salery
        else:
            raise ValueError
        
    @classmethod
    def create_from_string(cls,string):
        name, family = string.split("-")
        return cls(name, family)
    
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
# emp_1 = Employee('amir','attary')
# emp_2 = Employee('hasan','ajamy')

date = datetime.datetime.now()

emp_3 = Employee.create_from_string('amir-attary')
print(emp_3.is_workday(date))
print(emp_3.full_name())

# print("before")
# # print(emp_1.full_name(),' - ',emp_1.salery)
# # print(emp_2.full_name(),' - ',emp_2.salery)

# Employee.raise_salery(6000)

# print("after")
# print(emp_1.full_name(),' - ',emp_1.salery)
# print(emp_2.full_name(),' - ',emp_2.salery)