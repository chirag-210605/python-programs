
class A: 
    def show(self): 
        print("Method in Class A") 
class B(A): 
    def show(self): 
        print("Method in Class B") 
class C(A): 
    def show(self): 
        print("Method in Class C") 
class D(B, C): 
    pass 
# Creating an instance of Class D 
d = D() 
d.show()  # Calls the `show` method according to MRO 
# Display the Method Resolution Order 
print("Method Resolution Order for D:", D.__mro__)
