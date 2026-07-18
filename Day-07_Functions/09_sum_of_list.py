# Sum of List

def find_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


numbers = [12, 45, 8, 90, 32]

result = find_sum(numbers)

print(result)
