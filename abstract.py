import random
import string
from abc import ABC, abstractmethod

# Abstract class with the generate method
class PasswordGenerator(ABC):
    
    @abstractmethod
    def generate(self):
        pass

# Class to generate a password with letters only
class LettersOnlyPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        return ''.join(random.choices(string.ascii_letters, k=20))

# Class to generate a password with numbers only
class NumbersOnlyPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        return ''.join(random.choices(string.digits, k=20))

# Class to generate a password with both numbers and letters
class AlphanumericPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=20))

# Testing the classes
if __name__ == "__main__":
    letter_generator = LettersOnlyPasswordGenerator()
    print("Letters only password:", letter_generator.generate())

    number_generator = NumbersOnlyPasswordGenerator()
    print("Numbers only password:", number_generator.generate())

    alphanumeric_generator = AlphanumericPasswordGenerator()
    print("Alphanumeric password:", alphanumeric_generator.generate())

    