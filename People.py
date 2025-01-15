class People:
    
    def __init__(self):
        self.name = ""
        
    def take_input(self):
        
        self.user_input = input("Enter some text: ")
    
    def print_uppercase(self):
        
        print(self.user_input.upper())
        
user_input_obj = People()


user_input_obj.take_input()


user_input_obj.print_uppercase()
        

