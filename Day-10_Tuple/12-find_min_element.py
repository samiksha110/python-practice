# Write a program to find the smallest element in the tuple without using min().

numbers = (12, 45, 8, 90, 32)

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)
