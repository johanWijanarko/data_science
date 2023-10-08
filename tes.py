print("Hello World!")
a = 3
b = 4
c = a+b 
print(c)
age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

print('============')

x = 6
print(type(x))

x = "6"
print(type(x))

data =  """
    hello bro
    """
print(data)

# add index
x = 'Dicoding'
print(x[0])

# memoyong 2 index di depanx = 'Dicoding'
print(x[2:])


# intersection atau irisan
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {8, 4, 11, 12, 13}

union = set1.union(set2).union(set3)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection (set1 and set2):", intersection)

intersection2 = set1.intersection(set2).intersection(set3)
print("Intersection (set1, set2, and set3):", intersection2)

x3 = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x3 ['Job'] = "Web Developer"

print(x3)

del x3['age']

print(x3)