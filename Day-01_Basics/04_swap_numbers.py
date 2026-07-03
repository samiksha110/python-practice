# 4] swapping of numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Before swapping:")
# print(a, b)

# a, b = b, a

# print("After swapping:")
# print(a, b)

x = 10      # x becomes 10
y = x       # y becomes whatever x is
a = b       # a becomes whatever b is
b = temp    # b becomes whatever temp is