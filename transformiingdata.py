import math
ages = [15, 22, 34, 40, 65, 18, 23, 30, 45, 50]
# Add 5 years to each age
add_5_years = list(map(lambda age: age + 5, ages))
print(add_5_years) 

# Halve each age
halve_ages = list(map(lambda age: age / 2, ages))
print(halve_ages) 

# Convert each age to its square root
sqrt_ages = list(map(lambda age: math.sqrt(age), ages))
print(sqrt_ages)
