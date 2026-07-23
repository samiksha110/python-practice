# find second largest element in tuple

numbers = (12, 45, 8, 90, 32)

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest:
        second_largest = num

print(second_largest)
