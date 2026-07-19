# Check if a List Contains Duplicates

def has_duplicates(numbers):
    if len(numbers) == len(set(numbers)):
        return False
    else:
        return True


print(has_duplicates([10, 20, 30, 20, 40]))
