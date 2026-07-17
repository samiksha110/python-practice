# Count how many even numbers are in the list.

numbers = [12, 45, 8, 90, 32]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)
