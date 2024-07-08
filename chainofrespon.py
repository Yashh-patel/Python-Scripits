import math


def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, -6, 8, 9, 10, 11, 12, 13, 14, 15]

# Filter pipeline
pipeline = filter(is_even, numbers)
pipeline = filter(is_positive, pipeline)
pipeline = filter(is_prime, pipeline)

print(list(pipeline)) 
