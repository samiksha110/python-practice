# Find all occurrences of a number.
numbers = [12, 45, 8, 90, 32, 90, 12]

target = 90

for i in range(len(numbers)):
    if numbers[i] == target:
        print(i)
