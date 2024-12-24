import random

# Generate three random numbers in the range of 1 to 12
numbers = [random.randint(1, 12) for _ in range(3)]

# Print the numbers on one line
print(*numbers)
