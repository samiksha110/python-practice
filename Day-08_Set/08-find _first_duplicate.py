# Find the First Duplicate
# numbers = [10, 20, 30, 20, 40, 30]


numbers = [10, 20, 30, 20, 40, 30]

seen = set()

for num in numbers:
    if num in seen:
        print(num)
        break
    else:
        seen.add(num)
