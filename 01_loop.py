age = int(input("Enter your age: "))

if age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
else:
    print("You are a senior citizen")
