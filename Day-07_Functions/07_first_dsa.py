# Earlier, you solved this without functions:

# numbers = [12, 45, 8, 90, 32]

# Now write a function:

# def find_largest(numbers):

# It should:

# Find the largest number in the list.
# Return it.


def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [12, 45, 8, 90, 32]

result = find_largest(numbers)

print(result)
