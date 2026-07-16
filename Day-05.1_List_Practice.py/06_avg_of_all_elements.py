# Find the average of all elements without using sum().

numbers = [12, 45, 8, 90, 32]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print(average)
