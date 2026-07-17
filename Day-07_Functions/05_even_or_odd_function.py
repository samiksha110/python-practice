# Problem 5: Even or Odd Function
# Question

# Write a function named:

# is_even(n)

# It should:

# Return True if the number is even.
# Return False if the number is odd.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(is_even(8))
print(is_even(7))
