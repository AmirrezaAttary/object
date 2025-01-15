class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        return f'Name: {self.name}, Age: {self.age}'
    
    
a = Person('amir',12 )

print(a.display())
    
class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name, age)
        self.major = major
    
    def displayStudent(self):
        return super().display() + f', Major: {self.major}'
        
a = Student('amir',12 , 'Student')

print(a.displayStudent())