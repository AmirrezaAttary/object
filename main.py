class Car:
    def __init__(self,):
        self.color = "red"
        self.__speed = 200

    def set_speed(self,new_speed):
        self.__speed = new_speed
        
    
    def get_speed(self):
        return self.__speed
        
peride = Car()   

print(peride.get_speed())

peride.set_speed(500)

print(peride.get_speed())
        
# class Car:
#     def __init__(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
        
# peride = Car()
        
# print(peride.a)
# print(peride._b)
# print(peride.__c)    

  