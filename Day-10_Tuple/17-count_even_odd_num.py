# Count Even and Odd Numbers

numbers = (10, 21, 32, 45, 56)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd)
