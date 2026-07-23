# Write a program to find the largest number in the tuple without using max().

numbers = (12, 45, 8, 90, 32)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)
