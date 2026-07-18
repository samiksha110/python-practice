# It should return the smallest number in the list.

def find_smallest(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


numbers = [12, 45, 8, 90, 32]

result = find_smallest(numbers)

print(result)
