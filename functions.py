#def greet(name):
   # return f"Hello, {name}!"

#print(greet("lana"))

def Convert_toC(temp):
    Celtemp=(temp-32)*(5/9)
    return Celtemp

def Convert_toF(temp):
    Fehtemp=(temp*9/5) + 32
    return Fehtemp

print(f"{511}°F is {Convert_toC(511):.2f}°C")
print(f"{32}°C is {Convert_toF(32):.2f}°F")

