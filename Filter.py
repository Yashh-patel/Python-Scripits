ages = [15, 22, 34, 40, 65, 18, 23, 30, 45, 50]

# Less than 20
less_than_20 = list(filter(lambda age: age < 20, ages))
print(less_than_20) 

# Between 20 and 40
between_20_and_40 = list(filter(lambda age: 20 <= age <= 40, ages))
print(between_20_and_40) 

# Greater than 40
greater_than_40 = list(filter(lambda age: age > 40, ages))
print(greater_than_40) 
