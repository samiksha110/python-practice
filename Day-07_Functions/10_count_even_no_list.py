# It should return how many even numbers are in the list.

def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count


numbers = [12, 45, 8, 90, 32]

result = count_even(numbers)

print(result)
