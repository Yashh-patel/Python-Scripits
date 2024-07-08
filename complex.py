from functools import reduce

ages = [15, 22, 34, 40, 65, 18, 23, 30, 45, 50]


product_of_ages = reduce(lambda x, y: x * y, ages)
print("Product of all ages:", product_of_ages) 


def napply(funcs, x):
    for func in funcs:
        x = func(x)
    return x

# Testing napply
f1 = lambda x: x + 2
f2 = lambda x: x * 2
f3 = lambda x: x - 3

print("Result of napply:", napply([f1, f2, f3], 5))  
