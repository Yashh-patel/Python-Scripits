import math

from functools import reduce


def compose(func,num1,num2):
    return func(num1,num2)


def adder(num1,num2):
    return num1+num2


print(compose(adder,5,8))




ages = [23,56,224,12,21,34,56]


ages_below_20 = list(filter(lambda n:n<20,ages))
ages_between_20_40 = list(filter(lambda n:n<40 and n>=20,ages))
ages_above_40 = list(filter(lambda n:n>40,ages))

print(ages_below_20," then",ages_between_20_40, " then ", ages_above_40)



add5 = list(map(lambda n : n +5,ages))
half = list(map(lambda n : n/2,ages))
sqrt = list(map(lambda n : math.sqrt(n),ages))

print(add5," then",half, " then ", sqrt)


result = reduce(lambda n,m:n*m, ages)


print(result)