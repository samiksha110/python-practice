📚 Quick Cheat Sheet


> Function
def greet():
    print("Hello")

greet()



> Parameter
def greet(name):
    print("Hello", name)

greet("Samiksha")



> Return
def add(a, b):
    return a + b

result = add(5, 3)



> Default Parameter
def greet(name="Guest"):
    print("Hello", name)



> Keyword Arguments
student(age=22, name="Rahul")



> Local vs Global
x = 100

def demo():
    x = 50
    print(x)

print(x)
