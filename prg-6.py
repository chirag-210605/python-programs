
class ComplexNumber: 
    def __init__(self, real, imaginary): 
        self.real = real 
        self.imaginary = imaginary 
# Overloading the + operator 
    def __add__(self, other): 
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary) 
# Overloading the - operator 
    def __sub__(self, other): 
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary) 
# Overloading the * operator 
    def __mul__(self, other): 
        real_part = self.real * other.real - self.imaginary * other.imaginary 
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real 
        return ComplexNumber(real_part, imaginary_part) 
# Method to display the complex number 
    def __str__(self): 
        return f"{self.real} + {self.imaginary}i" 
# Example usage: 
complex1 = ComplexNumber(3, 2) 
complex2 = ComplexNumber(1, 7) 
# Addition 
print("Addition:", complex1 + complex2) 
# Subtraction 
print("Subtraction:", complex1 - complex2) 
# Multiplication 
print("Multiplication:", complex1 * complex2)
