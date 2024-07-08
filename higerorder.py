def alternator(f, g, lst):
    return [f(x) if i % 2 == 0 else g(x) for i, x in enumerate(lst)]


f = lambda x: x * 2
g = lambda x: x - 2
lst = [1, 2, 3, 4, 5]

print(alternator(f, g, lst)) 
