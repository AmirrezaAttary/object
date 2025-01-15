class Empoloyee:
    salery = 3000
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def hello(self):
        return 'hello'
    
    
    def __str__(self):
       return self.name
   
    def __repr__(self):
       return self.__class__.__name__
   
    def __add__(self, other):
        return self.salery + other.salery
      
emp1 = Empoloyee('amir',29)
emp2 = Empoloyee('ali',30)

print(emp1)
print(emp2.__repr__())
print(emp1+emp2)


