# Reverse a Tuple , Without using: [::-1] , reversed()

numbers = (10, 20, 30, 40)

result = []

for i in range(len(numbers)-1, -1, -1):
    result.append(numbers[i])

result = tuple(result)

print(result)
