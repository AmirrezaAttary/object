class Dog:
    quantity = 0
    def __init__(self, name, age):
        Dog.quantity += 1
        self.name = name
        self.age = age

bulldog = Dog("Sammy",3) 
hosky = Dog("Alex",5)

hosky.quantity = 1
print(Dog.quantity)
print(hosky.quantity)


""" 

باید هربار بعد از ورود یک سگ جدید
یک واحد به کلاس وریبل به وسیله آبجکت
اضافه کنیم

"""