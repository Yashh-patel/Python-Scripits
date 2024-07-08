
ages = [15, 22, 34, 40, 65, 18, 23, 30, 45, 50]
def compose(f, g):
    return lambda x: f(g(x))

# Testing compose
f = lambda x: x + 2
g = lambda x: x * 3

h = compose(f, g)
print(h(3)) 
