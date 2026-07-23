# Write a program to remove duplicates from a tuple.

numbers = (10, 20, 20, 30, 10, 40)

result = []
seen = set()

for num in numbers:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(tuple(result))


# numbers = (10, 20, 20, 30, 10, 40)

# unique = set(numbers)

# result = tuple(unique)

# print(result)
